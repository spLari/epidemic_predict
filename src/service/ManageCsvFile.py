'''
Service to handle with csv file.
'''
import os
import pandas
import sys

from ..helper import Constants as const

def getCsvFileData(filename):
  file = const.CSV_FILE_ROOT_DIRECTORY + filename
  fileExists = checkIfFileExists(file)
  if (not fileExists):
    sys.exit("An error occur: The file not exists.")

  csv_file = pandas.read_csv(file)
  return csv_file

def checkIfFileExists(file):
  return os.path.isfile(file)
    