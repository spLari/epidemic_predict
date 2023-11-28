'''
Service to handle with csv file.
'''
import os
import pandas
import sys

from ..helper import Constants as const

'''
Get the data from csv file.

Parameters:
  filename: the name of csv file.
Returns:
  A dataframe with csv data.
'''
def getCsvFileData(filename):
  file = const.CSV_FILE_ROOT_DIRECTORY + filename
  fileExists = checkIfFileExists(file)
  if (not fileExists):
    sys.exit("An error occur: The file not exists.")

  csv_file = pandas.read_csv(file)
  return csv_file

'''
Function to check if the file exists.

Parameters:
  file: the relative path of csv path.
Returns:
  A boolean value validating that file exists or not.
'''
def checkIfFileExists(file):
  return os.path.isfile(file)
    