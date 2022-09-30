import requests
import os
from twilio.rest import Client

url = "http://api.openweathermap.org/data/2.5/weather"
my_twilio_phone_number = ""
my_phone_number = ''

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
api_key = os.environ['OWN_API_KEY']

city = "Budapest"
params = {
    "q": city,
    "appid": api_key
}

# Due to issues with OpenCall I did that task on weather api
response = requests.get(url=url, params=params)
response.raise_for_status()
weather_data = response.json()


def it_rains():
    return weather_data['weather'][0]['id'] < 700


client = Client(account_sid, auth_token)
if it_rains():
    message = client.messages.create(
        body="It is raining outside ",
        from_=my_twilio_phone_number,
        to=my_phone_number
    )
else:
    message = client.messages.create(
        body="It is not raining outside ",
        from_=my_twilio_phone_number,
        to=my_phone_number
    )
print(message.sid)
