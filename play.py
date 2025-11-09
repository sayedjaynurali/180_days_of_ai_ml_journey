import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv() 

owm_api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("TWILIO_AUTH_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
phone_number = os.environ.get("OWN_PHONE_NUMBER")

endpoint_link = f"https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": 23.5020342,
    "lon": 100.7110063,
    "appid": owm_api_key,
    "cnt": 4
    }

# response = requests.get(url=endpoint_link,params=parameters)
# response.raise_for_status()
# data = response.json()

# for i in range(len(data["list"])):
#     if data["list"][i]["weather"][0]["id"] < 700: # API doc if it will rain the code is below 700

#         client = Client(account_sid, auth_token)
#         message = client.messages.create(
#         messaging_service_sid='MG5d36fae6f78286d5c04c8fd2add10f51',
#         body='\nHey!\nPlease Take an Umbrella\nIt might Rain today.',
#         to=phone_number
#         )
#         print(message.status)

#         break
