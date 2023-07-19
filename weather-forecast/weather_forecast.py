import requests
import pandas as pd
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=39.76&lon=-98.5#.XXFLaygzaUk')

soup = BeautifulSoup(page.content, 'html.parser')

week = soup.find(id = 'seven-day-forecast-body')
items = week.select('.tombstone-container')

# print(items[1])

# print(items[1].find(class_ = 'period-name').get_text())
# print(items[1].find(class_ = 'short-desc').get_text())
# print(items[1].find(class_ = 'temp').get_text())

period_name = [item.find(class_ = 'period-name').get_text() for item in items]
short_desc = [item.find(class_ = 'short-desc').get_text() for item in items]
temp_high = [item.find(class_ = 'temp').get_text() for item in items]
# print(period_name)
# print(short_desc)
# print(temp_high)

wether_stuff = pd.DataFrame({
    'period': period_name,
    'short_desc': short_desc,
    'temperatures': temp_high,
})

print(wether_stuff)

wether_stuff.to_csv('weather_forecast.csv')
