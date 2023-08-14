# HTTP Status Code
def verify_http_status_code(data, expected_data):
    assert data.status_code == int(expected_data), "Expected HTTP Status:" + expected_data


# Any Key, should not be null, or empty
def verify_key(key):
    assert key != 0, "Key is not Empty:" + key
    assert key > 0, "Key is greater than zero:" + key


# Token should not be null or empty
def verify_token(token):
    assert token is not None, "Token is not empty:" + token
    # assert token > 0, "Key is greater than zero:" + token
    # TypeError: '>' not supported between instances of 'str' and 'int'


# To check created booking_id is updated
def verify_bookingID(data, expected_data):
    assert data == expected_data, "Created booking id updated:" + expected_data


# To check created booking name updated
def verify_updated_firstname(data, expected_data):
    assert data == expected_data, "Created booking name updated:" + expected_data


# To check status message
def verify_status_message(data, expected_data):
    assert data == expected_data, "Expected status message displayed:" + expected_data
