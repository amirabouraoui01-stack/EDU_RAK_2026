Option Explicit

Sub Main()

On Error GoTo Failed

Dim f As Integer

Dim s As String

Dim detail As String

f = FreeFile

Open "C:/Users/amira/Desktop/projet_kicad/EDU_RAK_2026/VeillePorte/cst/veilleporte_868_reference.log" For Output As #f

Print #f, "RUN_STARTED"

Close #f

s = ""

s = s & "StoreParameter ""cap_x"", ""12.3""" & vbCrLf

s = s & "StoreParameter ""x_feed"", ""6""" & vbCrLf

s = s & "StoreParameter ""y_fourth"", ""58""" & vbCrLf

s = s & "StoreParameter ""x_last"", ""2""" & vbCrLf

s = s & "StoreParameter ""y_third"", ""53""" & vbCrLf

s = s & "StoreParameter ""x_end"", ""28.67""" & vbCrLf

s = s & "StoreParameter ""pcb_x"", ""30""" & vbCrLf

s = s & "StoreParameter ""pcb_y"", ""60""" & vbCrLf

s = s & "StoreParameter ""pcb_h"", ""0.8""" & vbCrLf

s = s & "StoreParameter ""cu_t"", ""0.035""" & vbCrLf

s = s & "StoreParameter ""gnd_y"", ""40""" & vbCrLf

s = s & "StoreParameter ""feed_gap"", ""0.5""" & vbCrLf

s = s & "StoreParameter ""track_w"", ""1""" & vbCrLf

s = s & "StoreParameter ""x_left"", ""2""" & vbCrLf

s = s & "StoreParameter ""x_right"", ""28.67""" & vbCrLf

s = s & "StoreParameter ""y_first"", ""43""" & vbCrLf

s = s & "StoreParameter ""y_second"", ""48""" & vbCrLf

s = s & "StoreParameter ""eps_r"", ""4.3""" & vbCrLf

s = s & "StoreParameter ""loss_tan"", ""0.02""" & vbCrLf

s = s & "StoreParameter ""f_target"", ""0.868""" & vbCrLf

s = s & "With Units" & vbCrLf

s = s & ".Geometry ""mm""" & vbCrLf

s = s & ".Frequency ""GHz""" & vbCrLf

s = s & ".Time ""ns""" & vbCrLf

s = s & "End With" & vbCrLf

s = s & "WCS.ActivateWCS ""global""" & vbCrLf

s = s & "With Material" & vbCrLf

s = s & ".Reset" & vbCrLf

s = s & ".Name ""FR4_VeillePorte""" & vbCrLf

s = s & ".Type ""Normal""" & vbCrLf

s = s & ".Epsilon ""eps_r""" & vbCrLf

s = s & ".Mue ""1""" & vbCrLf

s = s & ".TanD ""loss_tan""" & vbCrLf

s = s & ".TanDFreq ""f_target""" & vbCrLf

s = s & ".TanDGiven ""True""" & vbCrLf

s = s & ".Create" & vbCrLf

s = s & "End With" & vbCrLf

s = s & "With Brick" & vbCrLf

s = s & ".Reset" & vbCrLf

s = s & ".Name ""PCB""" & vbCrLf

s = s & ".Component ""VeillePorte""" & vbCrLf

s = s & ".Material ""FR4_VeillePorte""" & vbCrLf

s = s & ".Xrange ""0"", ""pcb_x""" & vbCrLf

s = s & ".Yrange ""0"", ""pcb_y""" & vbCrLf

s = s & ".Zrange ""0"", ""pcb_h""" & vbCrLf

s = s & ".Create" & vbCrLf

s = s & "End With" & vbCrLf

s = s & "With Brick" & vbCrLf

s = s & ".Reset" & vbCrLf

s = s & ".Name ""GND_top""" & vbCrLf

s = s & ".Component ""VeillePorte""" & vbCrLf

s = s & ".Material ""PEC""" & vbCrLf

s = s & ".Xrange ""0"", ""pcb_x""" & vbCrLf

s = s & ".Yrange ""0"", ""gnd_y""" & vbCrLf

s = s & ".Zrange ""pcb_h"", ""pcb_h+cu_t""" & vbCrLf

s = s & ".Create" & vbCrLf

s = s & "End With" & vbCrLf

s = s & "With Brick" & vbCrLf

s = s & ".Reset" & vbCrLf

s = s & ".Name ""GND_bottom""" & vbCrLf

s = s & ".Component ""VeillePorte""" & vbCrLf

s = s & ".Material ""PEC""" & vbCrLf

s = s & ".Xrange ""0"", ""pcb_x""" & vbCrLf

s = s & ".Yrange ""0"", ""gnd_y""" & vbCrLf

s = s & ".Zrange ""-cu_t"", ""0""" & vbCrLf

s = s & ".Create" & vbCrLf

s = s & "End With" & vbCrLf

s = s & "With Brick" & vbCrLf

s = s & ".Reset" & vbCrLf

s = s & ".Name ""GND_bridge""" & vbCrLf

s = s & ".Component ""VeillePorte""" & vbCrLf

s = s & ".Material ""PEC""" & vbCrLf

s = s & ".Xrange ""14.5"", ""15.5""" & vbCrLf

s = s & ".Yrange ""38"", ""39""" & vbCrLf

s = s & ".Zrange ""-cu_t"", ""pcb_h+cu_t""" & vbCrLf

s = s & ".Create" & vbCrLf

s = s & "End With" & vbCrLf

s = s & "Solid.Add ""VeillePorte:GND_top"", ""VeillePorte:GND_bridge""" & vbCrLf

s = s & "Solid.Add ""VeillePorte:GND_top"", ""VeillePorte:GND_bottom""" & vbCrLf

s = s & "With Brick" & vbCrLf

s = s & ".Reset" & vbCrLf

s = s & ".Name ""Antenna""" & vbCrLf

s = s & ".Component ""VeillePorte""" & vbCrLf

s = s & ".Material ""PEC""" & vbCrLf

s = s & ".Xrange ""x_left-track_w/2"", ""x_left+track_w/2""" & vbCrLf

s = s & ".Yrange ""gnd_y+feed_gap"", ""y_first+track_w/2""" & vbCrLf

s = s & ".Zrange ""pcb_h"", ""pcb_h+cu_t""" & vbCrLf

s = s & ".Create" & vbCrLf

s = s & "End With" & vbCrLf

s = s & "With Brick" & vbCrLf

s = s & ".Reset" & vbCrLf

s = s & ".Name ""Arm_1""" & vbCrLf

s = s & ".Component ""VeillePorte""" & vbCrLf

s = s & ".Material ""PEC""" & vbCrLf

s = s & ".Xrange ""x_left-track_w/2"", ""x_right+track_w/2""" & vbCrLf

s = s & ".Yrange ""y_first-track_w/2"", ""y_first+track_w/2""" & vbCrLf

s = s & ".Zrange ""pcb_h"", ""pcb_h+cu_t""" & vbCrLf

s = s & ".Create" & vbCrLf

s = s & "End With" & vbCrLf

s = s & "With Brick" & vbCrLf

s = s & ".Reset" & vbCrLf

s = s & ".Name ""Bend""" & vbCrLf

s = s & ".Component ""VeillePorte""" & vbCrLf

s = s & ".Material ""PEC""" & vbCrLf

s = s & ".Xrange ""x_right-track_w/2"", ""x_right+track_w/2""" & vbCrLf

s = s & ".Yrange ""y_first-track_w/2"", ""y_second+track_w/2""" & vbCrLf

s = s & ".Zrange ""pcb_h"", ""pcb_h+cu_t""" & vbCrLf

s = s & ".Create" & vbCrLf

s = s & "End With" & vbCrLf

s = s & "With Brick" & vbCrLf

s = s & ".Reset" & vbCrLf

s = s & ".Name ""Arm_2""" & vbCrLf

s = s & ".Component ""VeillePorte""" & vbCrLf

s = s & ".Material ""PEC""" & vbCrLf

s = s & ".Xrange ""x_left-track_w/2"", ""x_right+track_w/2""" & vbCrLf

s = s & ".Yrange ""y_second-track_w/2"", ""y_second+track_w/2""" & vbCrLf

s = s & ".Zrange ""pcb_h"", ""pcb_h+cu_t""" & vbCrLf

s = s & ".Create" & vbCrLf

s = s & "End With" & vbCrLf

s = s & "Solid.Add ""VeillePorte:Antenna"", ""VeillePorte:Arm_1""" & vbCrLf

s = s & "Solid.Add ""VeillePorte:Antenna"", ""VeillePorte:Bend""" & vbCrLf

s = s & "Solid.Add ""VeillePorte:Antenna"", ""VeillePorte:Arm_2""" & vbCrLf

s = s & "With Brick" & vbCrLf

s = s & ".Reset" & vbCrLf

s = s & ".Name ""Bend_2""" & vbCrLf

s = s & ".Component ""VeillePorte""" & vbCrLf

s = s & ".Material ""PEC""" & vbCrLf

s = s & ".Xrange ""x_left-track_w/2"", ""x_left+track_w/2""" & vbCrLf

s = s & ".Yrange ""y_second-track_w/2"", ""y_third+track_w/2""" & vbCrLf

s = s & ".Zrange ""pcb_h"", ""pcb_h+cu_t""" & vbCrLf

s = s & ".Create" & vbCrLf

s = s & "End With" & vbCrLf

s = s & "With Brick" & vbCrLf

s = s & ".Reset" & vbCrLf

s = s & ".Name ""Arm_3""" & vbCrLf

s = s & ".Component ""VeillePorte""" & vbCrLf

s = s & ".Material ""PEC""" & vbCrLf

s = s & ".Xrange ""x_left-track_w/2"", ""x_end+track_w/2""" & vbCrLf

s = s & ".Yrange ""y_third-track_w/2"", ""y_third+track_w/2""" & vbCrLf

s = s & ".Zrange ""pcb_h"", ""pcb_h+cu_t""" & vbCrLf

s = s & ".Create" & vbCrLf

s = s & "End With" & vbCrLf

s = s & "Solid.Add ""VeillePorte:Antenna"", ""VeillePorte:Bend_2""" & vbCrLf

s = s & "Solid.Add ""VeillePorte:Antenna"", ""VeillePorte:Arm_3""" & vbCrLf

s = s & "With Brick" & vbCrLf

s = s & ".Reset" & vbCrLf

s = s & ".Name ""Bend_3""" & vbCrLf

s = s & ".Component ""VeillePorte""" & vbCrLf

s = s & ".Material ""PEC""" & vbCrLf

s = s & ".Xrange ""x_right-track_w/2"", ""x_right+track_w/2""" & vbCrLf

s = s & ".Yrange ""y_third-track_w/2"", ""y_fourth+track_w/2""" & vbCrLf

s = s & ".Zrange ""pcb_h"", ""pcb_h+cu_t""" & vbCrLf

s = s & ".Create" & vbCrLf

s = s & "End With" & vbCrLf

s = s & "Solid.Add ""VeillePorte:Antenna"", ""VeillePorte:Bend_3""" & vbCrLf

s = s & "With Brick" & vbCrLf

s = s & ".Reset" & vbCrLf

s = s & ".Name ""Arm_4""" & vbCrLf

s = s & ".Component ""VeillePorte""" & vbCrLf

s = s & ".Material ""PEC""" & vbCrLf

s = s & ".Xrange ""x_last-track_w/2"", ""x_right+track_w/2""" & vbCrLf

s = s & ".Yrange ""y_fourth-track_w/2"", ""y_fourth+track_w/2""" & vbCrLf

s = s & ".Zrange ""pcb_h"", ""pcb_h+cu_t""" & vbCrLf

s = s & ".Create" & vbCrLf

s = s & "End With" & vbCrLf

s = s & "Solid.Add ""VeillePorte:Antenna"", ""VeillePorte:Arm_4""" & vbCrLf

s = s & "With Brick" & vbCrLf

s = s & ".Reset" & vbCrLf

s = s & ".Name ""Short_IFA""" & vbCrLf

s = s & ".Component ""VeillePorte""" & vbCrLf

s = s & ".Material ""PEC""" & vbCrLf

s = s & ".Xrange ""x_left-track_w/2"", ""x_left+track_w/2""" & vbCrLf

s = s & ".Yrange ""gnd_y"", ""y_first+track_w/2""" & vbCrLf

s = s & ".Zrange ""pcb_h"", ""pcb_h+cu_t""" & vbCrLf

s = s & ".Create" & vbCrLf

s = s & "End With" & vbCrLf

s = s & "Solid.Add ""VeillePorte:Antenna"", ""VeillePorte:Short_IFA""" & vbCrLf

s = s & "With Brick" & vbCrLf

s = s & ".Reset" & vbCrLf

s = s & ".Name ""Feed_IFA""" & vbCrLf

s = s & ".Component ""VeillePorte""" & vbCrLf

s = s & ".Material ""PEC""" & vbCrLf

s = s & ".Xrange ""x_feed-track_w/2"", ""x_feed+track_w/2""" & vbCrLf

s = s & ".Yrange ""gnd_y+feed_gap"", ""y_first+track_w/2""" & vbCrLf

s = s & ".Zrange ""pcb_h"", ""pcb_h+cu_t""" & vbCrLf

s = s & ".Create" & vbCrLf

s = s & "End With" & vbCrLf

s = s & "Solid.Add ""VeillePorte:Antenna"", ""VeillePorte:Feed_IFA""" & vbCrLf

s = s & "With Brick" & vbCrLf

s = s & ".Reset" & vbCrLf

s = s & ".Name ""Terminal_cap""" & vbCrLf

s = s & ".Component ""VeillePorte""" & vbCrLf

s = s & ".Material ""PEC""" & vbCrLf

s = s & ".Xrange ""0.5"", ""cap_x""" & vbCrLf

s = s & ".Yrange ""54.5"", ""59.5""" & vbCrLf

s = s & ".Zrange ""pcb_h"", ""pcb_h+cu_t""" & vbCrLf

s = s & ".Create" & vbCrLf

s = s & "End With" & vbCrLf

s = s & "Solid.Add ""VeillePorte:Antenna"", ""VeillePorte:Terminal_cap""" & vbCrLf

s = s & "With DiscretePort" & vbCrLf

s = s & ".Reset" & vbCrLf

s = s & ".PortNumber ""1""" & vbCrLf

s = s & ".Type ""SParameter""" & vbCrLf

s = s & ".Impedance ""50""" & vbCrLf

s = s & ".SetP1 ""False"", ""x_feed"", ""gnd_y"", ""pcb_h+cu_t/2""" & vbCrLf

s = s & ".SetP2 ""False"", ""x_feed"", ""gnd_y+feed_gap"", ""pcb_h+cu_t/2""" & vbCrLf

s = s & ".LocalCoordinates ""False""" & vbCrLf

s = s & ".InvertDirection ""False""" & vbCrLf

s = s & ".Monitor ""True""" & vbCrLf

s = s & ".Create" & vbCrLf

s = s & "End With" & vbCrLf

s = s & "Solver.FrequencyRange ""0.6"", ""1.136""" & vbCrLf

s = s & "With Boundary" & vbCrLf

s = s & ".Xmin ""expanded open""" & vbCrLf

s = s & ".Xmax ""expanded open""" & vbCrLf

s = s & ".Ymin ""expanded open""" & vbCrLf

s = s & ".Ymax ""expanded open""" & vbCrLf

s = s & ".Zmin ""expanded open""" & vbCrLf

s = s & ".Zmax ""expanded open""" & vbCrLf

s = s & "End With" & vbCrLf

s = s & "With Monitor" & vbCrLf

s = s & ".Reset" & vbCrLf

s = s & ".Name ""farfield (f=0.868)""" & vbCrLf

s = s & ".Domain ""Frequency""" & vbCrLf

s = s & ".FieldType ""Farfield""" & vbCrLf

s = s & ".Frequency ""0.868""" & vbCrLf

s = s & ".Create" & vbCrLf

s = s & "End With" & vbCrLf

s = s & "Plot.ZoomToStructure" & vbCrLf

s = s & "ChangeSolverType ""HF Time Domain""" & vbCrLf

s = s & "With Background" & vbCrLf

s = s & ".Reset" & vbCrLf

s = s & ".Type ""Normal""" & vbCrLf

s = s & ".Epsilon ""1""" & vbCrLf

s = s & ".Mu ""1""" & vbCrLf

s = s & "End With" & vbCrLf

s = s & "With MeshSettings" & vbCrLf

s = s & ".SetMeshType ""Hex""" & vbCrLf

s = s & ".Set ""StepsPerWaveNear"", ""13""" & vbCrLf

s = s & ".Set ""WavelengthRefinementSameAsNear"", ""1""" & vbCrLf

s = s & ".Set ""StepsPerBoxNear"", ""16""" & vbCrLf

s = s & "End With" & vbCrLf

s = s & "With Solver" & vbCrLf

s = s & ".CalculationType ""TD-S""" & vbCrLf

s = s & ".StimulationPort ""All""" & vbCrLf

s = s & ".StimulationMode ""All""" & vbCrLf

s = s & ".SteadyStateLimit ""-40""" & vbCrLf

s = s & "End With" & vbCrLf

AddToHistory "VeillePorte - IFA capacite terminale", s

SaveAs "C:/Users/amira/Desktop/projet_kicad/EDU_RAK_2026/VeillePorte/cst/veilleporte_868_reference.cst", True

f = FreeFile

Open "C:/Users/amira/Desktop/projet_kicad/EDU_RAK_2026/VeillePorte/cst/veilleporte_868_reference.log" For Append As #f

Print #f, "MODEL_BUILT"

Close #f

Solver.Start

Save

SelectTreeItem "1D Results\S-Parameters\S1,1"

With ASCIIExport

.Reset

.FileName "C:/Users/amira/Desktop/projet_kicad/EDU_RAK_2026/VeillePorte/cst/s11_veilleporte_868_reference.txt"

.Execute

End With

f = FreeFile

Open "C:/Users/amira/Desktop/projet_kicad/EDU_RAK_2026/VeillePorte/cst/veilleporte_868_reference.log" For Append As #f

Print #f, "S11_EXPORTED"

Close #f

Exit Sub

Failed:

detail = Err.Description

f = FreeFile

Open "C:/Users/amira/Desktop/projet_kicad/EDU_RAK_2026/VeillePorte/cst/veilleporte_868_reference.log" For Append As #f

Print #f, "ERROR: " & detail

Close #f

End Sub
