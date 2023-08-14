# Try to update on a delete id
from src.constants.apiconstants import url_create_token, url_create_booking, url_delete_booking
from src.helpers.api_wrapper import post_request, delete_request
from src.helpers.common_verification import verify_http_status_code, verify_token, verify_key
from src.helpers.payload_manager import payload_create_booking
from src.helpers.utils import common_headers, common_auth, headers_withToken

booking_id = None
token = None


class TestIntegration(object):

    def test_create_token(self):
        global token
        response = post_request(url_create_token(), headers=common_headers(), auth=None, payload=common_auth(),
                                in_json=False)
        verify_http_status_code(response, 200)
        token = response.json()["token"]
        verify_token(token)
        return token

    def test_create_booking(self):
        global booking_id
        response = post_request(url_create_booking(), headers=common_headers(), auth=None,
                                payload=payload_create_booking(), in_json=False)
        verify_http_status_code(response, 200)
        booking_id = response.json()["bookingid"]
        verify_key(booking_id)
        return booking_id

    def test_delete_booking(self):
        response = delete_request(url_delete_booking(booking_id), headers=headers_withToken(token), auth=None,
                                  in_json=False)
        verify_http_status_code(response, 201)
