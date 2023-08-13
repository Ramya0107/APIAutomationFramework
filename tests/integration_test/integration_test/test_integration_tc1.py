import pytest
import allure

from src.constants.apiconstants import url_create_token, url_create_booking, url_delete_booking, url_update_booking
from src.helpers.api_wrapper import post_request, put_request, delete_request
from src.helpers.common_verification import verify_http_status_code, verify_token, verify_key
from src.helpers.payload_manager import payload_create_booking, payload_updateAllData_booking
from src.helpers.utils import common_headers, headers_withToken, common_auth


class TestIntegration(object):

    @pytest.mark.integration
    @allure.feature("#TC1 creating a token")
    def test_create_token(self):
        global token
        response = post_request(url_create_token(), headers=common_headers(), auth=None, payload=common_auth(),
                                in_json=False)
        verify_http_status_code(response, 200)
        token = response.json()["token"]
        verify_token(token)
        return token

    @pytest.mark.integration
    @allure.feature("#TC2 creating a bookingID")
    def test_create_booking(self):
        global booking_id
        # call the functions to make request
        # you will not see how we are making a request in the test case
        response = post_request(url_create_booking(), headers=common_headers(), auth=None,
                                payload=payload_create_booking(), in_json=False)
        verify_http_status_code(response, 200)
        print(response.text)
        booking_id = response.json()["bookingid"]
        verify_key(booking_id)
        return booking_id

    @pytest.mark.integration
    @allure.feature("#TC3 updating full data in created bookingID")
    def test_update_booking(self):
        response = put_request(url_update_booking(booking_id),
                               headers=headers_withToken(token), auth=None,
                               payload=payload_updateAllData_booking(), in_json=False)
        verify_http_status_code(response, 200)
        print(response.text)

    @pytest.mark.integration
    @allure.feature("#TC4 deleting the created bookingID")
    def test_delete_booking(self):
        response = delete_request(url_delete_booking(booking_id),
                                  headers=headers_withToken(token), auth=None, in_json=False)
        verify_http_status_code(response, 201)
