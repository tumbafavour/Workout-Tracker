import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 60
HEIGHT_CM = 188.976
AGE = 19

APP_ID = ""
API_KEY = ""

USERNAME = "tumba"
PASSWORD = "1234567890"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/c2315d52ce09add7472e5c215d759180/myWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

GOOGLE_SHEET_NAME = "workout"

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(USERNAME, PASSWORD)
    )

    print(f"Sheety Response:\n {sheet_response.text}")
