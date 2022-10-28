import requests
from datetime import datetime

nutritionix_app_id = '40903e6f'
nutritionix_api_key = '1da813da5fd2d2996f110797cafbca8b'

sheety_url = 'https://api.sheety.co/5fcf9dc404a75c0dc69f46f5bb0151b0/workoutTracking/workouts'

user_input = input('Tell me what exercises you did today? ')

nutritionix_headers = {
    'x-app-id': nutritionix_app_id,
    'x-app-key': nutritionix_api_key,
}

sheety_aut = {
    'Authorization': 'Bearer #asdasdsafwerrfjdhbsfyugrgueDBADSAFGH'
}

nutritionix_params = {
    'query': user_input
}

post_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
response = requests.post(url=post_endpoint, json=nutritionix_params, headers=nutritionix_headers)

data = response.json()
exercise_data = data['exercises']
for x in exercise_data:
    exercise_name = x['name']
    duration = x['duration_min']
    calories = x['nf_calories']
    today = datetime.now()
    time = today.time()
    day = today.day
    month = today.month
    year = today.year

    sheety_response = requests.post(url=sheety_url, json={
        'workout': {
            'date': f'{day}/{month}/{year}',
            'time': time.strftime('%X'),
            'exercise': str(exercise_name).title(),
            'duration': duration,
            'calories': calories
        }
    }, headers=sheety_aut)

    print(sheety_response.text)
