'''
Service to manipulate data from csv file.
'''
from ..helper import Mapper

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

def removeSlash(string):
   return string.split("/")

def updateDictionary(dictCities, city, monthName):
  value = 1
  if monthName in dictCities[city]:
    value = dictCities[city][monthName] + 1

  dictCities[city].update({monthName: value})
  return dictCities

def setTotalCases(dictCities):
  city_keys = dictCities.keys()
  for city in city_keys:
    #print(dictCities[city].values())
    amount_monthly_cases = dictCities[city].values()
    totalCases = sum(amount_monthly_cases)
    dictCities[city].update({"Total Cases": totalCases})

  return dictCities
   
def createCitiesDictionary(dictData):
  dictCities = {}
  dictValues = dictData.values()
  for item in dictValues:
    city = item['City']
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