import sys
from src.service import HandleWithCsvData
from src.service import ManageCsvFile
from src.service import DataClassification
from src.service import Graphs

def validateNumberOfParameters():
    num_parameters = len(sys.argv)
    if (num_parameters != 2):
        sys.exit("An error occur: Invalid parameters number")

validateNumberOfParameters()

# Get the name of the database file.
filename = sys.argv[1]
# Read the csv file data.
csvFileData = ManageCsvFile.getCsvFileData(filename)
# Put the csv data in a dictionary.
dictData = HandleWithCsvData.createDataDictionary(csvFileData)
# Creating the dictionary to cluster the cities.
dictCities = HandleWithCsvData.createCitiesDictionary(dictData)
dictCities = DataClassification.setEpidemicSituation(dictCities)
# Graphs.plotMonthlyGrap("BELO HORIZONTE", dictCities)
# Graphs.plotCitiesGrap(dictCities)

for city in dictCities:
    situation = dictCities[city].get('SITUATION')
    if situation == "MODERATE" or situation == "HIGH" or situation == "VERY HIGH":
        print('Was detected an increase of cases in ' + city + ' in the last 3 months')
