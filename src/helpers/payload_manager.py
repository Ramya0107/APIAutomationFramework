# In future we can replace this from the excel or JSON

def payload_create_booking():
    payload = {
        "firstname": "Bruno",
        "lastname": "Br",
        "totalprice": 111,
        "depositpaid": "True",
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload


def payload_updateAllData_booking():
    payload = {
        "firstname": "Ramya",
        "lastname": "Uva",
        "totalprice": 200,
        "depositpaid": "False",
        "bookingdates": {
            "checkin": "2020-01-01",
            "checkout": "2023-01-01"
        },
        "additionalneeds": "Breakfast,Lunch"
    }
    return payload
