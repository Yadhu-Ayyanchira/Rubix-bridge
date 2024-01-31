import requests

api_url = 'http://localhost:5050/api/savedatatoken'
json_data = {
    "name": "value1",
    "test": "value2"
}

response = requests.post(api_url, json=json_data)

print(response.status_code)  # Print the HTTP status code
print(response.json())       # Print the response JSON
