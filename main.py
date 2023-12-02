import sys
import re

from src.service import HandleWithCsvData
from src.service import ManageCsvFile
from src.service import DataClassification
from src.service import Graphs
from src.service import GenerateReport

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
# Classify the situation of each city.
dictCities = DataClassification.setEpidemicSituation(dictCities)
# Generate report file.
folder = re.sub(".csv","",filename)
GenerateReport.logResultData(dictCities, folder)
# Create the graphs.
Graphs.plotMonthlyGrap("BELO HORIZONTE", dictCities, folder)
Graphs.plotCitiesGrap(dictCities, folder)
