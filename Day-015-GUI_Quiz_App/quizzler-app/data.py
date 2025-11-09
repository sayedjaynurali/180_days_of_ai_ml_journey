import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

question_data_response = requests.get("https://opentdb.com/api.php", params=parameters)
question_data_response.raise_for_status()
question_data = question_data_response.json()["results"]