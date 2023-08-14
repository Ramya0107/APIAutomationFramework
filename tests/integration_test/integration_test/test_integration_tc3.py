# Create a booking, delete it and verify
import pytest
import allure
from src.constants.apiconstants import url_create_booking, url_delete_booking, url_create_token, url_get_booking
from src.helpers.api_wrapper import post_request, delete_request, get_request
from src.helpers.common_verification import verify_http_status_code, verify_token, verify_key, verify_status_message
from src.helpers.payload_manager import payload_create_booking
from src.helpers.utils import common_headers, headers_withToken, common_auth

booking_id = None
token = None


class TestIntegration(object):

    @pytest.mark.july24_TC2_smoke
    @allure.feature("#1 creating a token")
    def test_create_token(self):
        global token
        response = post_request(url_create_token(), headers=common_headers(), auth=None, payload=common_auth(),
                                in_json=False)
        verify_http_status_code(response, 200)
        token = response.json()["token"]
        verify_token(token)
        return token

    @pytest.mark.july24_TC2_smoke
    @allure.feature("#2 create booking")
    def test_create_booking(self):
        global booking_id
        response = post_request(url_create_booking(), headers=common_headers(), auth=None,
                                payload=payload_create_booking(), in_json=False)
        verify_http_status_code(response, 200)
        booking_id = response.json()["bookingid"]
        verify_key(booking_id)
        return booking_id

    @pytest.mark.july24_TC2_smoke
    @allure.feature("#3 delete booking")
    def test_delete_booking(self):
        response = delete_request(url_delete_booking(booking_id), headers=headers_withToken(token), auth=None,
                                  in_json=False)
        verify_http_status_code(response, 201)

    @pytest.mark.july24_TC2_smoke
    @allure.feature("#4 deleted booking should not be available")
    def test_get_booking(self):
        response = get_request(url_get_booking(booking_id), headers=common_headers(), in_json=False)
        verify_http_status_code(response, 404)
        verify_status_message(response.text, "Not Found")
