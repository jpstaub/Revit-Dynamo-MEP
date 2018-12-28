#!/usr/env python

# This python script is meant to process full Trane TRACE System Component Selection files in CSV format.
# When this module is run it asks the operator for an input file through
# a typical directory GUI. The module also asks for an output file name
# through a typical save-as GUI. See "Set up CSV reader" to set the column numbers
# for the data of interest. Script returns Room Numbers and data of interest
# in CSV format. See def main() to enable/disable output of data.

import sys
import csv
import re

from Tkinter import Tk
from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing

# Set up input variable for the script
filenameIn = askopenfilename(initialdir='\\ripcord-nas0.ripcord\\Ripcord_Engineering\\projects')
input = filenameIn

# Set up output variable for the script
filenameOut = asksaveasfilename(defaultextension='.csv', filetypes=[("csv","*.csv")], initialdir='\\ripcord-nas0.ripcord\\Ripcord_Engineering\\projects')
output = filenameOut

# Example syntax for network file system appears below:
# output = r"\\ripcord-nas0.ripcord\\Ripcord_Engineering\\Projects\\2018\\18-002 Falmouth Memorial Library\\11_BIM\\Design_Process\\_Energy\\gbxml\\OutdoorAirflow.csv"

# Set up CSV reader
spaceColumn = 1 # Column number for spaces
# Cooling coil
clColumn = 1 # Column number for cooling coil tags
clTotColumn = 8 # Column number for total cooling capacity data
clSenColumn = 12 # Column number for sensible cooling capacity data
clEDBColumn = 19 # Column number for cooling EDB data
clEWBColumn = 21 # Column number for cooling EWB data
clEHRColumn = 25 # Column number for cooling HR data
clLDBColumn = 28 # Column number for cooling EDB data
clLWBColumn = 29 # Column number for cooling EWB data
clLHRColumn = 33 # Column number for cooling HR data
# Heating coil
htColumn = 51 # Column number for heating coil tags
htTotColumn = 54 # Column number for total heating capacity data
htEDBColumn = 63 # Column number for heating EDB data
htLDBColumn = 66 # Column number for heating LDB data
# Airflow
airflowTagColumn = 55 # Column number for airflow tags
airflowDataColumn = 58 # Column number for airflow data

# Set up data arrays
spaces = []
# Airflows
diffuser = []
nomVent = []
ahuVent = []
infil = []
retn = []
exhaust = []
rmExh = []
# Cooling coil
mainClTot = []
mainClSen = []
mainClEDB = []
mainClEWB = []
mainClEHR = []
mainClLDB = []
mainClLWB = []
mainClLHR = []
auxClTot = []
auxClSen = []
auxClEDB = []
auxClEWB = []
auxClEHR = []
auxClLDB = []
auxClLWB = []
auxClLHR = []
# Heating coil
mainHtCap = []
mainHtEDB = []
mainHtLDB = []
auxHtCap = []
auxHtEDB = []
auxHtLDB = []
# Results
results = []

# Read in data file
csvFileObj = open(input)
readerObj = csv.reader(csvFileObj)
sep = ' ' # Text separator to split column data on

# Start of fuction modules
def spaceNumbers():
  csvFileObj.seek(0) # This instruction resets the pointer from EOF (End Of File) to BOF for the next loop-based code block.
  for row in readerObj:
    if re.search('\d+', row[spaceColumn]):
      rest = row[spaceColumn].split(sep, 1)[0] # Removes space name from the column data for future processing with Dynamo script.
      spaces.append(rest)
  spacesOut = list(spaces) # Makes a copy of list of interest.
  spacesOut.insert(0,'Space') # Inserts data in front of the first list entry.
  results.append(spacesOut)
##  print spacesOut
  
def diffuserData():
  csvFileObj.seek(0)
  for row in readerObj:
    if row[airflowTagColumn] == 'Diffuser':
      diffuser.append(row[airflowDataColumn].replace(',',''))
  diffuserOut = list(diffuser)
  diffuserOut.insert(0,'Diffuser')
  results.append(diffuserOut)      
##  print diffuserOut  

def nomVentData():
  csvFileObj.seek(0)
  for row in readerObj:
    if row[airflowTagColumn] == 'Nom Vent':
      nomVent.append(row[airflowDataColumn].replace(',',''))
  nomVentOut = list(nomVent)
  nomVentOut.insert(0,'Nom Vent')
  results.append(nomVentOut)      
##  print nomVentOut

def ahuVentData():
  csvFileObj.seek(0)
  for row in readerObj:
    if row[airflowTagColumn] == 'AHU Vent':
      ahuVent.append(row[airflowDataColumn].replace(',',''))
  ahuVentOut = list(ahuVent)
  ahuVentOut.insert(0,'AHU Vent')
  results.append(ahuVentOut)      
##  print ahuVentOut

def infilData():
  csvFileObj.seek(0)
  for row in readerObj:
    if row[airflowTagColumn] == 'Infil':
      infil.append(row[airflowDataColumn].replace(',',''))
  infilOut = list(infil)
  infilOut.insert(0,'Infil')
  results.append(infilOut)      
##  print infilOut

def retnData():
  csvFileObj.seek(0)
  for row in readerObj:
    if row[airflowTagColumn] == 'AIRFLOWS':
      for row in readerObj:
        if row[airflowTagColumn] == 'Return':
          retn.append(row[airflowDataColumn].replace(',',''))
          break
  retnOut = list(retn)
  retnOut.insert(0,'Return')
  results.append(retnOut)      
##  print retnOut  

def exhaustData():
  csvFileObj.seek(0)
  for row in readerObj:
    if row[airflowTagColumn] == 'Exhaust':
      exhaust.append(row[airflowDataColumn].replace(',',''))
  exhaustOut = list(exhaust)
  exhaustOut.insert(0,'Exhaust')
  results.append(exhaustOut)      
##  print exhaustOut

def rmExhData():
  csvFileObj.seek(0)
  for row in readerObj:
    if row[airflowTagColumn] == 'Rm Exh':
      rmExh.append(row[airflowDataColumn].replace(',',''))
  rmExhOut = list(rmExh)
  rmExhOut.insert(0,'Rm Exh')
  results.append(rmExhOut)      
##  print rmExhOut

def mainClData():
  csvFileObj.seek(0)
  for row in readerObj:
    if row[clColumn] == 'Main Clg':
      mainClTot.append(row[clTotColumn].replace(',',''))
      mainClSen.append(row[clSenColumn].replace(',',''))
      mainClEDB.append(row[clEDBColumn].replace(',',''))
      mainClEWB.append(row[clEWBColumn].replace(',',''))
      mainClEHR.append(row[clEHRColumn].replace(',',''))
      mainClLDB.append(row[clLDBColumn].replace(',',''))
      mainClLWB.append(row[clLWBColumn].replace(',',''))
      mainClLHR.append(row[clLHRColumn].replace(',',''))
  mainClTotOut = list(mainClTot)
  mainClTotOut.insert(0,'Total Cap. Main Clg')
  mainClSenOut = list(mainClSen)
  mainClSenOut.insert(0,'Sensible Cap. Main Clg')
  mainClEDBOut = list(mainClEDB)
  mainClEDBOut.insert(0,'EDB Main Clg')
  mainClEWBOut = list(mainClEWB)
  mainClEWBOut.insert(0,'EWB Main Clg')
  mainClEHROut = list(mainClEHR)
  mainClEHROut.insert(0,'EHR Main Clg')
  mainClLDBOut = list(mainClLDB)
  mainClLDBOut.insert(0,'LDB Main Clg')
  mainClLWBOut = list(mainClLWB)
  mainClLWBOut.insert(0,'LWB Main Clg')
  mainClLHROut = list(mainClLHR)
  mainClLHROut.insert(0,'LHR Main Clg')      
  results.append(mainClTotOut)
  results.append(mainClSenOut)
  results.append(mainClEDBOut)
  results.append(mainClEWBOut)
  results.append(mainClEHROut)
  results.append(mainClLDBOut)
  results.append(mainClLWBOut)
  results.append(mainClLHROut)
##  print mainClTotOut
##  print mainClSenOut
##  print mainClEDBOut
##  print mainClEWBOut  
##  print mainClEHROut
##  print mainClLDBOut
##  print mainClLWBOut
##  print mainClLHROut

def auxClData():
  csvFileObj.seek(0)
  for row in readerObj:
    if row[clColumn] == 'Aux Clg':
      auxClTot.append(row[clTotColumn].replace(',',''))
      auxClSen.append(row[clSenColumn].replace(',',''))
      auxClEDB.append(row[clEDBColumn].replace(',',''))
      auxClEWB.append(row[clEWBColumn].replace(',',''))
      auxClEHR.append(row[clEHRColumn].replace(',',''))
      auxClLDB.append(row[clLDBColumn].replace(',',''))
      auxClLWB.append(row[clLWBColumn].replace(',',''))
      auxClLHR.append(row[clLHRColumn].replace(',',''))
  auxClTotOut = list(auxClTot)
  auxClTotOut.insert(0,'Total Cap. Aux Clg')
  auxClSenOut = list(auxClSen)
  auxClSenOut.insert(0,'Sensible Cap. Aux Clg')
  auxClEDBOut = list(auxClEDB)
  auxClEDBOut.insert(0,'EDB Aux Clg')
  auxClEWBOut = list(auxClEWB)
  auxClEWBOut.insert(0,'EWB Aux Clg')
  auxClEHROut = list(auxClEHR)
  auxClEHROut.insert(0,'EHR Aux Clg')
  auxClLDBOut = list(auxClLDB)
  auxClLDBOut.insert(0,'LDB Aux Clg')
  auxClLWBOut = list(auxClLWB)
  auxClLWBOut.insert(0,'LWB Aux Clg')
  auxClLHROut = list(auxClLHR)
  auxClLHROut.insert(0,'LHR Aux Clg')      
  results.append(auxClTotOut)
  results.append(auxClSenOut)
  results.append(auxClEDBOut)
  results.append(auxClEWBOut)
  results.append(auxClEHROut)
  results.append(auxClLDBOut)
  results.append(auxClLWBOut)
  results.append(auxClLHROut)
##  print auxClTotOut
##  print auxClSenOut
##  print auxClEDBOut
##  print auxClEWBOut  
##  print auxClEHROut
##  print auxClLDBOut
##  print auxClLWBOut
##  print auxClLHROut

def mainHtData():
  csvFileObj.seek(0)
  for row in readerObj:
    if row[htColumn] == 'Main Htg':
      mainHtCap.append(row[htTotColumn].replace(',',''))
      mainHtEDB.append(row[htEDBColumn].replace(',',''))
      mainHtLDB.append(row[htLDBColumn].replace(',',''))
  mainHtCapOut = list(mainHtCap)
  mainHtCapOut.insert(0,'Total Cap. Main Htg')
  mainHtEDBOut = list(mainHtEDB)
  mainHtEDBOut.insert(0,'EDB Main Htg')
  mainHtLDBOut = list(mainHtLDB)
  mainHtLDBOut.insert(0,'LDB Main Htg')     
  results.append(mainHtCapOut)
  results.append(mainHtEDBOut)
  results.append(mainHtLDBOut)
##  print mainHtCapOut
##  print mainHtEDBOut
##  print mainHtLDBOut

def auxHtData():
  csvFileObj.seek(0)
  for row in readerObj:
    if row[htColumn] == 'Aux Htg':
      auxHtCap.append(row[htTotColumn].replace(',',''))
      auxHtEDB.append(row[htEDBColumn].replace(',',''))
      auxHtLDB.append(row[htLDBColumn].replace(',',''))
  auxHtCapOut = list(auxHtCap)
  auxHtCapOut.insert(0,'Total Cap. Aux Htg')
  auxHtEDBOut = list(auxHtEDB)
  auxHtEDBOut.insert(0,'EDB Aux Htg')
  auxHtLDBOut = list(auxHtLDB)
  auxHtLDBOut.insert(0,'LDB Aux Htg')     
  results.append(auxHtCapOut)
  results.append(auxHtEDBOut)
  results.append(auxHtLDBOut)
##  print auxHtCapOut
##  print auxHtEDBOut
##  print auxHtLDBOut

# End of function modules  
  
def main(): # Comment out functions as required to enable/disable output of data.
  spaceNumbers()
  diffuserData()
  nomVentData()
##  ahuVentData()
  infilData()
  retnData()
  exhaustData()
  rmExhData()
  mainClData()
##  auxClData()
  mainHtData()
##  auxHtData()  

main()

# Writes results list to CSV file.
with open(output, "wb+") as resultFile:
	wr = csv.writer(resultFile, dialect='excel')
	wr.writerows(zip(*results))

csvFileObj.close()
exit()	

