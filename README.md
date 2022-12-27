# Revit-Dynamo-MEP
Ripcord Engineering developed utilities to improve the automation of MEP engineering in Autodesk Revit.

## Dynamo Graphs

### AutomatedBuildingEnergyModel (Tested - Revit 2021 / Dynamo 2.3)
A series of graphs that automate the generation of conceptual masses based on space volume geometry.

### AutomatedDaylightModel (Tested - Revit 2021 / Dynamo 2.3)
Automates the generation of conceptual masses for export as a 3D DWG in support of daylight modeling by [Velux Daylight Visualizer](https://www.velux.com/what-we-do/digital-tools/daylight-visualizer). 

To crop Velux Daylight Visualizer daylight report images for use as [underlays on plans](https://www.youtube.com/watch?v=J5ilicWeNCs):
* [Click here](https://github.com/jpstaub/imageProcess_streamlit) for online webapp details.

  OR
        
* See AutomatedDaylightModel python script below.

### TRACE700 (Tested - Revit 2021 / Dynamo 2.3):
Sets TRACE700 data from CSV file generated from TRACE700 Room Checksums into matching space parameters. See Python Scripts below for a Room Checksums processor to produce the prerequisite CSV file. 

## Python Scripts
### AutomatedDaylightModel >> imageProcessing.py (Tested - Windows10 / Python 3.10):
Processes [Velux Daylight Visualizer](https://www.velux.com/what-we-do/digital-tools/daylight-visualizer) report images. Processed images can be underlayed and scaled on background plans to give [architectural context](https://www.youtube.com/watch?v=J5ilicWeNCs) to Daylight Factor results.

### TRACE700 >> TRACE Room Checksums Full Processor.py (Tested - Windows10 / Python 2.7):
Processes full Trane TRACE700 System Component Selection input file in CSV format. The script returns Room Numbers and data of interest in CSV format for use in other programs like Revit.




