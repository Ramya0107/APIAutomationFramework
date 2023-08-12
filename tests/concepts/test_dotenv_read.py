import os

from dotenv import load_dotenv

load_dotenv()

import requests
import pytest

# # Create Token
# @pytest.fixture
# def test_post_token():
#     payload = {
#         "username": "admin",
#         "password": "password123"
#     }
#     headers = {
#         "Content-Type": "application/json"
#     }
#     response = requests.post("https://restful-booker.herokuapp.com/auth", headers=headers, json=payload)
#     assert response.status_code == 200
#     print(response.text)
#     # print(response.json()["token"])
#     return response.json()["token"]


# Create booking
BookingID = None


@pytest.fixture
def test_post_booking():
    global BookingID
    payload_post_req = {
        "firstname": "Bruno",
        "lastname": "Br",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post("https://restful-booker.herokuapp.com/booking", headers=headers, json=payload_post_req)
    assert response.status_code == 200
    print(response.text)
    BookingID = response.json()["bookingid"]
    return BookingID


# full update
def test_put_req(test_post_booking):
    global BookingID
    payload_put_req = {
        "firstname": "Bru",
        "lastname": "BrBr",
        "totalprice": 200,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2018-02-02",
            "checkout": "2019-02-02"
        },
        "additionalneeds": "Breakfast, Lunch"
    }
    temp_token = "token=" + os.getenv("token")
    print(temp_token)
    headers = {
        "Content-Type": "application/json",
        "Cookie": temp_token
    }
    url_put = "https://restful-booker.herokuapp.com/booking/" + str(BookingID)
    print(url_put)
    response = requests.put(url_put, headers=headers, json=payload_put_req)
    # print(response.status_code)
    print(response.text)
    assert response.status_code == 200
    # return response.json()["bookingid"]
    # print("patch ->", test_post_token, test_post_booking)

# get specific bookingID
# def test_get_bookingID(test_post_booking):
#     url_get_bookingID = "https://restful-booker.herokuapp.com/booking/" + test_post_booking
#     print(url_get_bookingID)
#     response = requests.get(url_get_bookingID)
#     print(response.text)
#     assert response.status_code == 200
#     assert len(response.json()) > 0


# def test_delete_req(test_post_token, test_post_booking):
#     temp_token = "token=" + test_post_token
#     # print(temp_token)
#     headers = {
#         "Content-Type": "application/json",
#         "Cookie": temp_token
#     }
#     url_delete = "https://restful-booker.herokuapp.com/booking/" + str(test_post_booking)
#     print(url_delete)
#     response = requests.delete(url_delete, headers=headers)
#     # print(response.status_code)
#     print(response.text)
#     print(response.status_code)
#     assert response.status_code == 201
