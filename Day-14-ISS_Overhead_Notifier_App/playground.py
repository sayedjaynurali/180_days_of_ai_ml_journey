import requests
import datetime as dt

my_lat = 22.750904
my_long = 88.375050

# response = requests.get(url="http://api.open-notify.org/iss-now.json")

# a = response.json()
# b = a["iss_position"]["latitude"]

# print(type(b))

now = dt.datetime.now(dt.timezone.utc)

parameters = {
    "lat": my_lat,
    "lng": my_long,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
response_json = response.json()
sunrise = response_json["results"]['sunrise'].split("T")[1].split(":")[0]
sunset = response_json["results"]['sunset'].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
print(now.hour)