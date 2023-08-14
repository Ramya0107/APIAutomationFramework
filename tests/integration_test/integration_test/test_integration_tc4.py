# Try to update on a delete id
import pytest
import allure
from src.constants.apiconstants import url_create_token, url_create_booking, url_delete_booking, url_update_booking
from src.helpers.api_wrapper import post_request, delete_request, patch_request
from src.helpers.common_verification import verify_http_status_code, verify_token, verify_key, verify_updated_firstname, \
    verify_status_message
from src.helpers.payload_manager import payload_create_booking, payload_updateRequestName
from src.helpers.utils import common_headers, common_auth, headers_withToken

booking_id = None
token = None


class TestIntegration(object):

    @pytest.mark.july24_TC3_smoke
    @allure.feature("#1 creating a token")
    def test_create_token(self):
        global token
        response = post_request(url_create_token(), headers=common_headers(), auth=None, payload=common_auth(),
                                in_json=False)
        verify_http_status_code(response, 200)
        token = response.json()["token"]
        verify_token(token)
        return token

    @pytest.mark.july24_TC3_smoke
    @allure.feature("#2 create booking")
    def test_create_booking(self):
        global booking_id
        response = post_request(url_create_booking(), headers=common_headers(), auth=None,
                                payload=payload_create_booking(), in_json=False)
        verify_http_status_code(response, 200)
        booking_id = response.json()["bookingid"]
        verify_key(booking_id)
        return booking_id

    @pytest.mark.july24_TC3_smoke
    @allure.feature("#3 delete booking")
    def test_delete_booking(self):
        response = delete_request(url_delete_booking(booking_id), headers=headers_withToken(token), auth=None,
                                  in_json=False)
        verify_http_status_code(response, 201)

    @pytest.mark.july24_TC1_smoke
    @allure.feature("#4 deleted booking should not be available for updating")
    def test_update_booking_name(self):
        response = patch_request(url_update_booking(booking_id), headers=headers_withToken(token), auth=None,
                                 payload=payload_updateRequestName(), in_json=False)
        verify_http_status_code(response, 405)
        verify_status_message(response.text, "Method Not Allowed")

