#! python3
import json, requests, sys

if len(sys.argv) < 2:
    print('Usage: quickweather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

url = 'http://api.openweathermap.org/data/2.5/weather?q=%s' % (location)
response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)

w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])