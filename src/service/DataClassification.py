from datetime import datetime
from ..helper import Mapper

'''
Function to set the key 'SITUATION' in dictionary.
This key will inform if the situation of epidemic in the city is normal, moderate, high, super high.

Parameters:
  dictCities: the dictionary mapped by cities.
Returns:
  The dictionary mapped by cities with new key.
'''
def setEpidemicSituation(dictCities):
  for city in dictCities:
    dict_city = dictCities[city]
    situation = getSituation(city, dict_city)
    dictCities[city].update({'SITUATION': situation})

  return dictCities

'''
Function to get epidemic situation of the city.

Parameters:
  cityName: the name of the city.
  cityData: the dictionary with values of the city.
Returns:
  A string with the situation.
'''
def getSituation(cityName, cityData):
  state_population = Mapper.getCitiesPopulation()
  if (not cityName in state_population):
    return 'INVALID'

  city_population = state_population[cityName]
  current_month = datetime.now().month
  percent = 0
  if (current_month != '01' or current_month != '02' or current_month != '03'):
    last_three_months = []
    subtrator = 1
    # Get the number of months mapped in city. -1 to remove the 'Total Cases' key.
    month_mapped_in_city = len(cityData.keys())-1

    # Define the number of months to search to calculate the percent.
    number_of_months_to_consider = 3 
    # Check the number of months in the dictionary.
    if month_mapped_in_city > 0 and month_mapped_in_city < 3:
      number_of_months_to_consider = month_mapped_in_city

    # Append the months inside the list to calculate.
    while len(last_three_months) < number_of_months_to_consider:
      month = current_month - subtrator
      month_name = Mapper.getMonthName(str(month))
      if month_name in cityData.keys():
        last_three_months.append(month_name)

      subtrator += 1

    for month in last_three_months:
      num_cases = cityData[month]
      percent += num_cases

    percent = percent*100/city_population

    ten_percent_of_population = city_population*10/100
    twenty_percent_of_population = city_population*20/100
    fourty_percent_of_population = city_population*40/100
    if (percent < ten_percent_of_population):
      return 'NORMAL'
    elif (percent >= ten_percent_of_population and percent < twenty_percent_of_population):
      return 'MODERATE'
    elif (percent >= twenty_percent_of_population and percent < fourty_percent_of_population):
      return 'HIGH'
    else:
      return 'VERY HIGH'
