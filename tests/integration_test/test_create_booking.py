'''
Author : Ramya
Ojective : Create and Verify by Post Request
TC#1 - Verify the Status Code, Headers
TC#2 - Verify the Body-> Booking ID
TC#3 - Verify the JSON schema is valid
'''
# test_create_booking_tc1 -> base url, create booking url, post request, payload

# import pytest

import sys

sys.path.append('/PyAPIAutomationFramework/src/')

from src.constants.apiconstants import url_create_booking
from src.helpers.api_wrapper import post_request
from src.helpers.common_verification import verify_key, verify_http_status_code
from src.helpers.payload_manager import payload_create_booking
from src.helpers.utils import common_headers


class TestIntegration(object):

    def test_create_booking_tc1(self):
        # call the functions to make request
        # you will not see how we are making a request in the
        response = post_request(url_create_booking(), headers=common_headers(), auth=None,
                                payload=payload_create_booking(), in_json=False)
        verify_http_status_code(response, 200)
        booking_id = response.json()["bookingid"]
        verify_key(booking_id)

    # def test_create_booking_tc2(self):
    #     assert True == True
    #
    # def test_create_booking_tc3(self):
    #     assert True == True
