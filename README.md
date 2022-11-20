# Revit-Dynamo-MEP
Ripcord Engineering developed utilities to improve the automation of MEP engineering in Autodesk Revit.

## Dynamo Graphs

### AutomatedBuildingEnergyModel (Tested - Revit 2021 / Dynamo 2.3)
A series of graphs that automate the generation of conceptual masses based on space volume geometry.

### AutomatedDaylightModel (Tested - Revit 2021 / Dynamo 2.3)
Automates the generation of conceptual masses for export as a 3D DWG in support of daylight modeling by Velux Daylight Visualizer. 

### TRACE700 (Tested - Revit 2021 / Dynamo 2.3):
Sets TRACE700 data from CSV file generated from TRACE700 Room Checksums into matching space parameters. See below for TRACE700 Room Checksums processor to produce required CSV file. 

## Python Scripts
### AutomatedDaylightModel >> imageProcessing.py (Tested - Windows10 / Python 3.10):
Processes Velux Daylight Visualizer report images. Processed images can be overlayed and scaled on background plans to give architectural context to Daylight Factor results.

### TRACE700 >> TRACE Room Checksums Full Processor.py (Tested - Windows10 / Python 2.7):
Processes full Trane TRACE700 System Component Selection input file in CSV format. The script returns Room Numbers and data of interest in CSV format for use in other programs like Revit.




