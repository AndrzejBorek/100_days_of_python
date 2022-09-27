import smtplib
import time

import requests
import datetime as dt

MY_LAT = 51.936619
MY_LNG = 15.508690


def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }
    url = "https://api.sunrise-sunset.org/json"
    response = requests.get(url=url, params=parameters)
    response.raise_for_status()
    data = response.json()
    time_now = dt.datetime.now()
    sunrise = data['results']['sunrise'].split('T')[1].split('+')[0]
    sunset = data['results']['sunset'].split('T')[1].split('+')[0]
    sunrise_hour = sunrise.split(":")[0]
    sunrise_minute = sunrise.split(":")[1]
    sunset_hour = sunset.split(":")[0]
    sunset_minute = sunset.split(":")[1]
    after_sunset = time_now.hour > sunset_hour or (time_now.hour == sunset_hour and time_now.minute >= sunset_minute)
    before_sunrise = time_now.hour < sunrise_hour or (
            time_now.hour == sunrise_hour and time_now.minute <= sunrise_minute)
    return after_sunset or before_sunrise

# while True:
#     time.sleep(60)
#     if is_dark() and is_overhead():
#          with smtplib.SMTP_SSL(google_id, port=465) as connection:
#             connection.login(user=my_email_gmail, password=app_password)
#             connection.sendmail(from_addr=my_email_gmail, to_addrs=my_email_gmail,
#                                 msg=f"Subject:ISS!\n\n Look up, ISS is overhead!".encode('utf-8'))
