import requests
from datetime import datetime,timezone
import smtplib
import time

my_email = "youremail@email.com"
my_password = "your_smtp_app_password"

MY_LAT = 22.572645 # Your latitude
MY_LONG = 88.363892 # Your longitude

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

#Your position is within +5 or -5 degrees of the ISS position.

def is_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now(timezone.utc)
    time_now_hour = time_now.hour

    if (time_now_hour >= sunset or time_now_hour <= sunrise) and MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LONG - 5 < iss_longitude < MY_LONG + 5:
        try:
            with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
                connection.starttls()
                connection.login(user=my_email,password=my_password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs="qrtwry@yahoo.com",
                    msg = f"Subject:ISS is Above You\n\nLookup its Night and The ISS is Above you"
                )
        
            print("Email Send Successfully")
    
        except smtplib.SMTPException as error:
                print(f"Error: Failed to send email to {my_email}.")
                print(f"Details: {error}")

while True:
    is_above()
    time.sleep(60)