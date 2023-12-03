'''
Service to manipulate data from csv file.
'''
from ..helper import Mapper

'''
Function to map the csv data into a dictionary.

Parameters:
  csvFileData: a dataframe with csv data.
Returns:
  A dictionary with the csv data.
'''
def createDataDictionary(csvFileData):
    dictData = {}
    for row in csvFileData.iterrows():
      values = row[1]
      locations = removeSlash(values['Location'])

      # Prevent to map a data with missing values.
      if (len(locations) != 4):
        continue

      dictData[values['Accession ID']] = {
        "Collection date": values['Collection date'],
        "Submission date": values['Submission date'],
        "Region": locations[0].strip().upper(),
        "Country": locations[1].strip().upper(),
        "State": locations[2].strip().upper(),
        "City": locations[3].strip().upper(),
      }
    
    return dictData

'''
Function to remove the forward slash symbol of a string.

Parameters:
  string: the string that will be splited
Returns:
  The string splited.
'''
def removeSlash(string):
   return string.split("/")

'''
Function to update the value of monthName key on dictionary.

Parameters:
  dictCities: the dictionary that will be updated.
  city: the current city that we are iterating.
  monthName: the monthName key that will be updated.
Returns:
  The name dictionary updated.
'''
def updateDictionary(dictCities, city, monthName):
  value = 1
  if monthName in dictCities[city]:
    value = dictCities[city][monthName] + 1

  dictCities[city].update({monthName: value})
  return dictCities

def setTotalCases(dictCities):
  city_keys = dictCities.keys()
  for city in city_keys:
    amount_monthly_cases = dictCities[city].values()
    totalCases = sum(amount_monthly_cases)
    dictCities[city].update({"Total Cases": totalCases})

  return dictCities

'''
Function to create a dictionary mapping by city.

Parameters:
  dictData: the dictionary with csvData.
Returns:
  The name dictionary mapped by cities.
'''
def createCitiesDictionary(dictData):
  dictCities = {}
  dictValues = dictData.values()
  for item in dictValues:
    city = item['City']
    mapped_population = Mapper.getCitiesPopulation()
    if (not city in mapped_population):
      continue
    date = removeSlash(item['Collection date'])
    month_name = Mapper.getMonthName(date[1])
    if city in dictCities:
      dictCities = updateDictionary(dictCities, city, month_name)
      continue
    dictCities[city] = {
      month_name: 1
    }

  setTotalCases(dictCities)  
  return dictCities