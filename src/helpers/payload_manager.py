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
