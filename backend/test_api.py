import requests

# URL of your running API
url = "http://127.0.0.1:8000/predict"

# Sample input data
data = {
    "age": 50,
    "sex": 1,
    "bmi": 30.0,
    "bp": 80,
    "s1": 150,
    "s2": 100,
    "s3": 50,
    "s4": 4.5,
    "s5": 5.5,
    "s6": 110
}

# Send POST request to the API
response = requests.post(url, json=data)

# Print the result
print("Response:", response.json())
