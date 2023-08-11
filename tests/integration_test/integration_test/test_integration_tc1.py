import pytest

from src.constants.apiconstants import url_create_token, url_create_booking, url_delete_booking, url_update_booking
from src.helpers.api_wrapper import post_request, put_request, delete_request
from src.helpers.common_verification import verify_http_status_code, verify_token, verify_key
from src.helpers.payload_manager import payload_create_booking, payload_updateAllData_booking
from src.helpers.utils import common_headers, headers_withToken, common_auth


class TestIntegration(object):

    @pytest.fixture
    def test_create_token(self):
        response = post_request(url_create_token(), headers=common_headers(), auth=None, payload=common_auth(),
                                in_json=False)
        verify_http_status_code(response, 200)
        token = response.json()["token"]
        verify_token(token)
        return token

    @pytest.fixture
    def test_create_booking(self):
        # call the functions to make request
        # you will not see how we are making a request in the test case
        response = post_request(url_create_booking(), headers=common_headers(), auth=None,
                                payload=payload_create_booking(), in_json=False)
        verify_http_status_code(response, 200)
        print(response.text)
        booking_id = response.json()["bookingid"]
        verify_key(booking_id)
        return booking_id

    def test_update_booking(self, test_create_token, test_create_booking):
        response = put_request(url_update_booking(test_create_booking),
                               headers=headers_withToken(test_create_token), auth=None,
                               payload=payload_updateAllData_booking(), in_json=False)
        verify_http_status_code(response, 200)
        print(response.text)

    def test_delete_booking(self, test_create_token, test_create_booking):
        response = delete_request(url_delete_booking(test_create_booking),
                                  headers=headers_withToken(test_create_token), auth=None, in_json=False)
        verify_http_status_code(response, 201)
