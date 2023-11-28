import sys
from src.service import HandleWithCsvData
from src.service import ManageCsvFile

def validateNumberOfParameters():
    num_parameters = len(sys.argv)
    if (num_parameters != 2):
        sys.exit("An error occur: Invalid parameters number")

validateNumberOfParameters()

# Get the name of the database file.
filename = sys.argv[1]
# Read the file data.
csvFileData = ManageCsvFile.getCsvFileData(filename)
# Put the data in a dictionary.
dicData = HandleWithCsvData.createDataDictionary(csvFileData)
