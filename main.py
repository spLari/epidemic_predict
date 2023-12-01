import sys
from src.service import HandleWithCsvData
from src.service import ManageCsvFile
from service import DataClassification

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
print(dictCities)
