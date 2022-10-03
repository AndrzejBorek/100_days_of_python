import datetime as dt
import requests

APP_ID = ""
APP_API_KEY = ""
MY_GENDER = "male"
MY_WEIGHT = "78"
MY_HEIGHT = "178"
MY_AGE = "24"
exercise_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

auth_sheety_header = {
    "Authorization": "Bearer "
}

auth_nutritionix_header = {
    "x-app-id": APP_ID,
    "x-app-key": APP_API_KEY,
    "x-remote-user-id": "0"
}

# Let user input his workout and translate it from natural language

workout = input("What workout did you had today?")

exercise_params = {
    "query": workout,
    "gender": MY_GENDER,
    "weight_kg": MY_WEIGHT,
    "height_cm": MY_HEIGHT,
    "age": MY_AGE
}
post_exercise_response = requests.post(headers=auth_nutritionix_header, url=exercise_url, json=exercise_params)
post_exercise_response.raise_for_status()

# Get workouts from sheet

get_workouts_url = ""
get_workouts_response = requests.get(url=get_workouts_url, headers=auth_sheety_header)
get_workouts_response.raise_for_status()

# Post workouts to sheet

post_workout_url = ""

Date = dt.datetime.now().strftime("%d/%m/%Y")
Time = dt.datetime.now().strftime("%X")

for exercise in post_exercise_response.json()["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": Date,
            "time": Time,
            "exercise": exercise['name'].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    post_workout_response = requests.post(url=post_workout_url, json=sheet_inputs, headers=auth_sheety_header)
    post_workout_response.raise_for_status()
