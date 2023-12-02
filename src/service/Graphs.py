import matplotlib.pyplot as plt

from ..helper import Constants as const
from ..service import GenerateReport as report

def plotMonthlyGrap(city, dictCities, folder):
  prepareReportDirectory(folder)
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

  # Plot
  plt.plot(x_axis, y_axis)

  # Save graph in report directory.
  path = const.REPORT_DIRECTORY + folder + '/'
  plt.savefig(path + 'Monitoring Report - ' + city)

  # Show the graph
  plt.show()

def plotCitiesGrap(dictCities, folder):
  prepareReportDirectory(folder)
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

  # Plot
  plt.xticks(rotation=90)
  plt.ylim(0, 600)
  plt.tight_layout(pad=1, w_pad=4, h_pad=5)
  plt.bar(x_axis, y_axis)

  # Save graph in report directory.
  path = const.REPORT_DIRECTORY + folder + '/'
  plt.savefig(path + 'Monitoring Report - All Cities')

  # Show the graph
  plt.show()

def prepareReportDirectory(folder):
  if not report.checkDirectoryExists(folder):
    report.createDirectory(folder)