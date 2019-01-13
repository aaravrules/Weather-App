import urllib.request
import json

key = "503ed57b27900c47536cbec6009d5475"
city = "Fremont"
url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=imperial&appid=" + key

json_string = urllib.request.urlopen(url).read()
json_data = json.loads(json_string)
print(json_data)


#draw the interface, api documentation
