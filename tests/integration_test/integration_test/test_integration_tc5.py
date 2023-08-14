# Get an existing booking id by using get all booking id's , update the booking and verify it by getting it

import pytest
import allure
from src.constants.apiconstants import url_create_token, url_getAll_booking, url_update_booking, url_get_booking
from src.helpers.api_wrapper import post_request, get_request, put_request
from src.helpers.common_verification import verify_http_status_code, verify_token, verify_bookingID
from src.helpers.payload_manager import payload_updateAllData_booking
from src.helpers.utils import common_headers, common_auth, headers_withToken

booking_id = None
token = None
updated_data = None


class TestIntegration(object):

    @pytest.mark.july24_TC4_smoke
    @allure.feature("#1 creating a token")
    def test_create_token(self):
        global token
        response = post_request(url_create_token(), headers=common_headers(), auth=None, payload=common_auth(),
                                in_json=False)
        verify_http_status_code(response, 200)
        token = response.json()["token"]
        verify_token(token)
        return token

    @pytest.mark.july24_TC4_smoke
    @allure.feature("#2 get all the booking id's")
    def test_getAll_booking(self):
        global booking_id
        response = get_request(url_getAll_booking(), headers=None, in_json=False)
        verify_http_status_code(response, 200)
        booking_id = response.json()[0]["bookingid"]
        print("First Booking ID:", booking_id)
        return booking_id

    @pytest.mark.july24_TC4_smoke
    @allure.feature("#3 update the full data of 1st booking id")
    def test_update_booking(self):
        global updated_data
        response = put_request(url_update_booking(booking_id), headers=headers_withToken(token), auth=None,
                               payload=payload_updateAllData_booking(), in_json=False)
        verify_http_status_code(response, 200)
        print(response.text)
        updated_data = response.json()
        return updated_data

    @pytest.mark.july24_TC4_smoke
    @allure.feature("#4 get the updated booking id and verify")
    def test_get_booking(self):
        response = get_request(url_get_booking(booking_id), headers=common_headers(), in_json=False)
        verify_http_status_code(response, 200)
        verify_bookingID(response.json(), updated_data)
        print(response.text)
