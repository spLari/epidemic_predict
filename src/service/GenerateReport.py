import os
import pandas as pd

from datetime import datetime
from ..helper import Constants as const

'''
Function to check if the report directory already exists.
Returns:
  Return True if directory exists and False if not exists.
'''
def checkDirectoryExists(folder):
  if os.path.exists(const.REPORT_DIRECTORY + folder + '/'):
    return True
  
  return False

'''
Function to create the report directory.
'''
def createDirectory(folder):
  directoryExists = checkDirectoryExists(folder)
  if not directoryExists:
    print('creating')
    os.makedirs(const.REPORT_DIRECTORY + '/' + folder + '/')

'''
Function to save the result in report directory.
'''
def logResultData(dictCities, folder):
  # Create report directory.
  createDirectory(folder)

  data = convertDictInDataframe(dictCities)

  # Save the value of all cities.
  saveFileOnDirectory(folder, data, "all_cities_report.csv")

  # Save the cities with epidemic situation detected.
  saveEpidemicCities(dictCities, folder)

'''
Function to convert dictionary in a Dataframe.

Returns:
  Return a dataframe object.
'''
def convertDictInDataframe(dictCities):
  df = pd.DataFrame.from_dict(dictCities)
  # Remove the NaN values
  df = df.fillna(0)
  return df

'''
Function to save the csv file the report directory.
Parameters:
  dataframe: the data that will be save in directory.
'''
def saveFileOnDirectory(folder, dataframe, fileName):
  dataframe.to_csv(const.REPORT_DIRECTORY + folder + '/' + fileName, encoding='utf-8')

'''
Function to get and save the cities that is in the epidemic risk situation.
Parameters:
  dictCities: the dictionary of the cities values.
'''
def saveEpidemicCities(dictCities, folder):
  for city in dictCities:
    epidemicCities = {}
    situation = dictCities[city].get('SITUATION')
    if situation == "MODERATE" or situation == "HIGH" or situation == "VERY HIGH":
        print('Was detected an increase of cases in ' + city + ' in the last 3 months')
        print(dictCities[city])
        epidemicCities.update({city: dictCities[city]})

  data = convertDictInDataframe(epidemicCities)
  saveFileOnDirectory(folder, data, "cities_with_epidemic.csv")
