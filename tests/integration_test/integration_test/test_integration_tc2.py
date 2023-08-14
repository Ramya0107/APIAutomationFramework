# Create a booking, update the booking name, get the booking id and verify
# update and get given only the response not the bookingid, so verified the response


from src.constants.apiconstants import url_create_booking, url_update_booking, url_get_booking, url_create_token
from src.helpers.api_wrapper import post_request, patch_request, get_request
from src.helpers.common_verification import verify_http_status_code, verify_key, verify_bookingID, verify_token, verify_updated_firstname
from src.helpers.payload_manager import payload_create_booking, payload_updateRequestName
from src.helpers.utils import common_headers, headers_withToken, common_auth

booking_id = None
token = None


class TestIntegration(object):

    def test_create_booking(self):
        global booking_id
        response = post_request(url_create_booking(), headers=common_headers(), auth=None,
                                payload=payload_create_booking(), in_json=False)
        verify_http_status_code(response, 200)
        booking_id = response.json()["bookingid"]
        verify_key(booking_id)
        return booking_id

    def test_create_token(self):
        global token
        response = post_request(url_create_token(), headers=common_headers(), auth=None, payload=common_auth(),
                                in_json=False)
        verify_http_status_code(response, 200)
        token = response.json()["token"]
        verify_token(token)
        return token

    def test_update_booking_name(self):
        global updated_data
        response = patch_request(url_update_booking(booking_id), headers=headers_withToken(token), auth=None,
                                 payload=payload_updateRequestName(), in_json=False)
        verify_http_status_code(response, 200)
        verify_updated_firstname(response.json()["firstname"], payload_updateRequestName()["firstname"])
        print(response.text)
        updated_data = response.json()
        return updated_data

    def test_get_booking(self):
        response = get_request(url_get_booking(booking_id), headers=common_headers(), in_json=False)
        verify_http_status_code(response, 200)
        verify_bookingID(response.json(), updated_data)
        print(response.text)
