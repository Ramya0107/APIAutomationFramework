# This helps to read the json files and provide the JSON data
import json


def get_payload_auth():
    # Read from the auth.json and return json
    file_data = open("src/resources/auth.json")
    data = json.loads(str(file_data))
    file_data.close()
    return data


def common_headers():
    headers = {
        "Content-Type": "application/json"
    }
    return headers


def common_auth():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload


def headers_withToken(test_create_token):
    temp_token = "token=" + test_create_token
    headers = {
        "Content-Type": "application/json",
        "Cookie": temp_token
    }
    return headers
