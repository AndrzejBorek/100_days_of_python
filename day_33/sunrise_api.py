import requests
from datetime import datetime

MY_LAT = 51.936619
MY_LNG = 15.508690

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}
url = "https://api.sunrise-sunset.org/json"
response = requests.get(url=url, params=parameters)
response.raise_for_status()
data = response.json()

time_now = datetime.now()

sunrise = data['results']['sunrise'].split('T')[1].split('+')[0]
sunset = data['results']['sunset'].split('T')[1].split('+')[0]

print(f"Sunrise {sunrise}")
print("Now is: {:02d}:{:02d}:{:02d}".format(time_now.hour, time_now.minute, time_now.second))
print(f"Sunset: {sunset}")
