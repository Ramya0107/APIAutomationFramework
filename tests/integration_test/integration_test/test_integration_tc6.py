# Create booking enter a wrong payload or json

import pytest
import allure

from src.constants.apiconstants import url_create_booking
from src.helpers.api_wrapper import post_request
from src.helpers.common_verification import verify_http_status_code, verify_status_message
from src.helpers.payload_manager import payload_create_req_empty, payload_create_req_withoutvalues
from src.helpers.utils import common_headers

booking_id = None


class TestIntegration():

    @pytest.mark.july24_TC4_smoke
    @allure.feature("#1 create request with empty payload")
    def test_create_booking_empty(self):
        response = post_request(url_create_booking(), headers=common_headers(), auth=None,
                                payload=payload_create_req_empty(), in_json=False)
        verify_http_status_code(response, 500)
        verify_status_message(response.text, "Internal Server Error")

    @pytest.mark.july24_TC4_smoke
    @allure.feature("#TC2 create request with invalid payload")
    def test_create_booking_invalid(self):
        response = post_request(url_create_booking(), headers=common_headers(), auth=None,
                                payload=payload_create_req_withoutvalues(), in_json=False)
        verify_http_status_code(response, 400)
        verify_status_message(response.text, "Bad Request")
