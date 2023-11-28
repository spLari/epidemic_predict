'''
Service to manipulate data from csv file.
'''
import sys

dicData = {}

def createDataDictionary(csvFileData):
    for row in csvFileData.iterrows():
      values = row[1]
      locations = splitLocation(values['Location'])

      # Prevent to map a data with missing values.
      if (len(locations) != 4):
        continue

      dicData[values['Accession ID']] = {
        "Collection date": values['Collection date'],
        "Submission date": values['Submission date'],
        "Region": locations[0].strip().upper(),
        "Country": locations[1].strip().upper(),
        "State": locations[2].strip().upper(),
        "City": locations[3].strip().upper(),
      }
    
    return dicData

def splitLocation(location):
   return location.split("/")