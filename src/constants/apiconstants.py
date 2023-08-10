# Add all the constants here

# Adding URL contants. Python is all about functions

def base_url():
    # Change based on the env.json - Stage, preprod, prod
    # In future i will write logic to change the base url based on the env
    return "https://restful-booker.herokuapp.com"


def url_create_token():
    return "https://restful-booker.herokuapp.com/auth"


def url_create_booking():
    return "https://restful-booker.herokuapp.com/booking"


def url_update_booking(booking_id):
    return "https://restful-booker.herokuapp.com/booking/"+str(booking_id)


def url_delete_booking(booking_id):
    return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)



