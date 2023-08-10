# HTTP Status Code

def verify_http_status_code(data, expected_data):
    assert data.status_code == int(expected_data), "Expected HTTP Status:" + expected_data


#Any Key, should not be null, or empty
def verify_key(key):
    assert key != 0, "Key is not Empty:" + key
    assert key > 0, "Key is greater than zero:" + key