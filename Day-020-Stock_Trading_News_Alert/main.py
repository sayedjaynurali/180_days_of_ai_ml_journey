import requests
from datetime import datetime, timedelta
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

account_sid = os.environ.get("TWILIO_AUTH_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
alpha_vantage_api_key = os.environ.get("ALPHA_VANTAGE_API_KEY")
news_api_key = os.environ.get("NEWSAPI_API_KEY")
phone_number = os.environ.get("OWN_PHONE_NUMBER")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

alpha_vantage_endpoint = "https://www.alphavantage.co/query?"
newsapi_endpoint = "https://newsapi.org/v2/everything?"

params_alpha = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alpha_vantage_api_key,
    "datatype": "json"
}

news_api_params = {
    "q": COMPANY_NAME,
    "pageSize": 3,
    "sortBy": "publishedAt",
    "apiKey": news_api_key,
    "language": "en"
} 

alpha_response = requests.get(alpha_vantage_endpoint,params=params_alpha)
alpha_response.raise_for_status()
alpha_data = alpha_response.json()

latest_date_str = alpha_data["Meta Data"]["3. Last Refreshed"]
date_obj = datetime.strptime(latest_date_str, '%Y-%m-%d')
previous_date = date_obj - timedelta(days=1)
previous_date_str = previous_date.strftime('%Y-%m-%d')

current_day_price = float(alpha_data['Time Series (Daily)'][latest_date_str]['4. close'])
previous_day_price = float(alpha_data['Time Series (Daily)'][previous_date_str]['4. close'])

percent_change = round((((current_day_price - previous_day_price)/previous_day_price)*100),2)

news_api_response = requests.get(newsapi_endpoint,params=news_api_params)
news_api_response.raise_for_status()
news_data = news_api_response.json()
print(news_data)

if (percent_change > 5) or (percent_change < -5): 
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    messaging_service_sid='MG5d36fae6f78286d5c04c8fd2add10f51',
    body=f'{STOCK}: {percent_change}%\nHeadlines: {news_data['articles'][0]['title']}',
    to=phone_number
    )
    print(message.status)
else:
    print(f"Don't worry. It just changed by {percent_change}%")

