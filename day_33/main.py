from datetime import datetime

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
time = datetime.fromtimestamp(response.json()['timestamp'])
print(f"It happened: {time}")
# print(response.json())
# print(response.json().keys())
longitude = response.json()['iss_position']['longitude']
latitude = response.json()['iss_position']['latitude']
iss_position = (longitude, latitude)
print(iss_position)
