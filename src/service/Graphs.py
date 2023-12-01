import matplotlib.pyplot as plt
import os

from ..helper import Constants as const

def plotMonthlyGrap(city, dictCities):
  createDirectory()
  x_axis = list(dictCities[city].keys())
  y_axis = list(dictCities[city].values())

  # Remove the 'SITUATION' key and value
  x_axis.pop()
  y_axis.pop()

  # Remove the 'Total Cases' key and value
  x_axis.pop()
  y_axis.pop()

  # Set labels
  plt.suptitle('Monitoring Report by month - ' + city)
  plt.xlabel('Month')
  plt.ylabel('Total Cases')
  #plot and show
  plt.plot(x_axis, y_axis)
  plt.show()
  plt.savefig(const.REPORT_DIRECTORY + 'Monitoring Report -' + city)

def plotCitiesGrap(dictCities):
  createDirectory()
  x_axis = []
  y_axis = []
  for city in dictCities:
    total_case = dictCities[city].get('Total Cases')

    x_axis.append(city)
    y_axis.append(total_case)

  # Set labels
  plt.suptitle('Monitoring Report - All Cities')
  plt.xlabel('City')
  plt.ylabel('Total Cases')

  # Plot and show
  plt.xticks(rotation=90)
  plt.ylim(0, 600)
  plt.tight_layout(pad=1, w_pad=4, h_pad=5)
  plt.bar(x_axis, y_axis)
  plt.show()
  plt.savefig(const.REPORT_DIRECTORY + 'Monitoring Report - All Cities')

def createDirectory():
  if not os.path.exists(const.REPORT_DIRECTORY):
    os.mkdir(const.REPORT_DIRECTORY)
    return True