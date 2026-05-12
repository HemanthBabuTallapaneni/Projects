import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 83
HEIGHT_CM = 183
AGE = 21
USERNAME = "hemanthbabu"
PASSWORD = "Hemanth@2004"

APP_ID = "app_8fa62a453b944fdebfa41aaa"
API_KEY = "nix_live_baV8RaZKMW4RSEs5z6Tc2dr9Gm5tzGHK"

exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheet_endpoint = "https://api.sheety.co/cbe8340a11c977c1dc77bc49c19caa10/workoutTracking/workouts"

exercise_text = input("Tell me what exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(exercise_endpoint, headers=headers, json=parameters)
result = response.json()

today_date = datetime.now().strftime("%Y/%m/%d")
now_date = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout":{
            "date": today_date,
            "time": now_date,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet = requests.post(sheet_endpoint,
                          json=sheet_inputs,
                          auth=(USERNAME, PASSWORD))
    print(sheet.text)
