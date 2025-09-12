# workout tracking project

import os
import requests
import datetime

# https://docs.google.com/spreadsheets/d/1DHL6Y8XAHSC_KhJsa9QMekwP8b4YheWZY_sxlH3i494/edit?gid=0#gid=0
# make a copy of this spread sheet

# https://www.nutritionix.com/business/api click get you api key and create account
NUTRITIONIX_APP_ID=os.getenv('NUTRITIONIX_APP_ID')
NUTRITIONIX_API_KEY=os.getenv('NUTRITIONIX_API_KEY')
SHEETY_AUTH=os.getenv('SHEETY_AUTH')

GENDER = 'male'
WEIGHT_KG = 70
HEIGHT_CM = 183
AGE = 23
today=datetime.datetime.now()

headers={
    'x-app-id':NUTRITIONIX_APP_ID,
    'x-app-key':NUTRITIONIX_API_KEY,
}
# https://docx.syndigo.com/developers/docs/getting-started-1 documentation
# https://trackapi.nutritionix.com/docs/#/default/post_v2_natural_exercise
nlp_for_exercise_endpoint='https://trackapi.nutritionix.com/v2/natural/exercise'

exercise=input('Tell me which exercise you did: ')
exercise_parameters={
    'query':exercise,
    'weight_kg':WEIGHT_KG,
    'height_cm':HEIGHT_CM,
    'age':AGE,
    'gender':GENDER
}
response=requests.post(url=nlp_for_exercise_endpoint,json=exercise_parameters,headers=headers)
data=response.json()['exercises']

# https://dashboard.sheety.co/login login to sheety with the same account you used for spread sheets
# '''
# Under your Google Account Security settings, you should see that Sheety has access.
# Double-check that you see Sheety listed as an authorized app.
# Otherwise, your Python code can't access your spreadsheet.
# In your project page, click on "New Project" and create a new project in Sheety
# with the name "Workout Tracking" and paste in the URL of your own "My Workouts" Google Sheet.
# if you permission error it is because When you logged in to Sheety
# you didn't check the last box which gave Sheety permission to write to spreadsheets.
# Go to the troubleshooting area and it tells you how to delete the permission given and try again and check the last checkbox.
# https://sheety.co/faqs/troubleshooting.html
# I hope this will help you guys, carry on learning!
# Click on the workouts API endpoint and enable GET and POST.
# '''
# https://sheety.co/docs/requests documentation
# Add either "Basic Authentication" or "Bearer Token" to your Sheety endpoint to secure it.

sheety_endpoint='https://api.sheety.co/01dba5432ddb3438f558f3fd502dd158/myWorkouts/workouts'
sheety_header={
    'Authorization':SHEETY_AUTH
}
for item in data:
    sheety_output={
        'workout':{
            'date':today.date().strftime("%d/%m/%Y"),
            'time':today.time().strftime('%H:%M:%S'),
            'exercise': item['name'].title(),
            'duration': item['duration_min'],
            'calories': item['nf_calories'],
        }
    }
    # all the keys of sheety workout should be lowercase even if you have column with upper case in you google sheets
    # all the values that are strings should be in camel case Ie. use title().
    response = requests.post(url=sheety_endpoint,json=sheety_output,headers=sheety_header)

