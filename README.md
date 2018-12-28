# Revit-Dynamo-MEP
Ripcord Engineering developed utilities to improve the automation of MEP engineering in Autodesk Revit.

## Dynamo Graphs
### SetAirTerminalAirflow (Tested - Revit 2018 / Dynamo 1.3): 
Takes the airflow values from space parameters, divides the airflow between the number of air terminals of a duct system type in a space, then sets the result in each air terminal. 

### SetSpaceNumberIntoRooms (Test - Revit 2018 / Dynamo 1.3):
Sets Space Numbers into a shared parameter <Space Number> in an ARCH project file so the Room Schedule in the MECH project file shows a correlation between MECH Spaces and ARCH Rooms.

### SetSpaceParameterListViaCsvFile (Test - Revit 2018 / Dynamo 1.3):
Takes columns of data from a CSV file and inserts it into Revit Spaces parameters. The graph writes all identified space parameters concurrently.


## Python Scripts


