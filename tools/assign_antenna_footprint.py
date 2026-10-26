from pathlib import Path
import json
import re
import uuid


class Atom(str):
    pass


def parse(source):
    tokens = re.findall(r'"(?:\\.|[^"\\])*"|[^\s()]+|[()]', source)
    stack = []
    root = None
    for token in tokens:
        if token == "(":
            node = []
            if stack:
                stack[-1].append(node)
            else:
                root = node
            stack.append(node)
        elif token == ")":
            stack.pop()
        else:
            stack[-1].append(json.loads(token, strict=False) if token.startswith('"') else Atom(token))
    if stack:
        raise ValueError("Parenthèses non équilibrées dans la schématique")
    return root


def kids(node, key):
    return [item for item in node if isinstance(item, list) and item and item[0] == key]


def one(node, key):
    return next(iter(kids(node, key)), None)


def dump(node):
    if isinstance(node, list):
        return "(" + " ".join(dump(item) for item in node) + ")"
    if isinstance(node, Atom):
        return str(node)
    return json.dumps(node, ensure_ascii=False)

project = Path(__file__).resolve().parents[1] / "VeillePorte"
schematic = project / "veilleporte_complet.kicad_sch"
footprint = "VeillePorte_Antennes:IFA_868_CST_30x20_PisteFine"
root = parse(schematic.read_text(encoding="utf-8"))
matches = [
    symbol
    for symbol in kids(root, "symbol")
    if any(prop[1] == "Reference" and prop[2] == "AE1" for prop in kids(symbol, "property"))
]
if len(matches) != 1:
    raise SystemExit(f"Attendu exactement un symbole AE1, trouve: {len(matches)}")
fields = kids(matches[0], "property")
field = next((prop for prop in fields if prop[1] == "Footprint"), None)
value_field = next((prop for prop in fields if prop[1] == "Value"), None)
if value_field is not None:
    value_field[2] = "Antenne IFA imprimée 868 MHz"
if field is None:
    matches[0].insert(3, [Atom("property"), "Footprint", footprint,
                           [Atom("at"), Atom("0"), Atom("0"), Atom("0")],
                           [Atom("effects"), [Atom("font"), [Atom("size"), Atom("1.27"), Atom("1.27")]], [Atom("hide"), Atom("yes")]]])
else:
    field[2] = footprint

# Make this modeled antenna a PCB item and add a matching ground pin for the
# footprint's second pad/net-tie. The RF pin keeps the existing /RF net.
for flag in kids(matches[0], "on_board"):
    flag[1] = Atom("yes")
else:
    matches[0].insert(4, [Atom("on_board"), Atom("yes")])

lib_id = next(item[1] for item in kids(matches[0], "lib_id"))
lib_symbol = next(item for item in kids(one(root, "lib_symbols"), "symbol") if item[1] == lib_id)
unit = next(item for item in kids(lib_symbol, "symbol") if item[1].endswith("_1_1"))
if not any(pin for pin in kids(unit, "pin") if one(pin, "number")[1] == "2"):
    unit.append([
        Atom("pin"), Atom("passive"), Atom("line"),
        [Atom("at"), Atom("0"), Atom("5.08"), Atom("270")], [Atom("length"), Atom("2.54")],
        [Atom("name"), "GND", [Atom("effects"), [Atom("font"), [Atom("size"), Atom("1.27"), Atom("1.27")]]]],
        [Atom("number"), "2", [Atom("effects"), [Atom("font"), [Atom("size"), Atom("1.27"), Atom("1.27")]]]],
    ])
pin2 = next((item for item in kids(matches[0], "pin") if item[1] == "2"), None)
instances_node = one(matches[0], "instances")
if pin2 is None:
    pin_node = [Atom("pin"), "2", [Atom("uuid"), str(uuid.uuid4())]]
    matches[0].insert(matches[0].index(instances_node), pin_node)
elif matches[0].index(pin2) > matches[0].index(instances_node):
    matches[0].remove(pin2)
    matches[0].insert(matches[0].index(instances_node), pin2)

instance_at = one(matches[0], "at")
x, y = float(instance_at[1]), float(instance_at[2])
labels = kids(root, "label")
for name, lx, ly in (("RF", x, y + 5.08), ("GND", x, y - 5.08)):
    if not any(label[1] == name and one(label, "at")[1:3] == [str(lx), str(ly)] for label in labels):
        label_node = [
            Atom("label"), name,
            [Atom("at"), Atom(f"{lx:.2f}"), Atom(f"{ly:.2f}"), Atom("0")],
            [Atom("effects"), [Atom("font"), [Atom("size"), Atom("1.27"), Atom("1.27")]], [Atom("justify"), Atom("left"), Atom("bottom")]],
            [Atom("uuid"), str(uuid.uuid4())],
        ]
        sheet_instances_node = one(root, "sheet_instances")
        root.insert(root.index(sheet_instances_node), label_node)
for label in list(kids(root, "label")):
    sheet_instances_node = one(root, "sheet_instances")
    if root.index(label) > root.index(sheet_instances_node):
        root.remove(label)
        root.insert(root.index(sheet_instances_node), label)
schematic.write_text(dump(root) + "\n", encoding="utf-8", newline="\n")
print(f"AE1 assigne a {footprint}; broches RF/GND presentes sur le PCB")
