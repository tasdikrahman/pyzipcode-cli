#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyzipcode import Pyzipcode as pz
import unittest
import sys
try:
    import simplejson as json
except ImportError:
    import json


class TestModule(unittest.TestCase):
    """Checks for the sanity of all module methods"""

    def test_ziptastic_valid_pincode_1(self):
        current_result = pz.query_ziptastic_api(603203, "IN")
        expected_result = {'postal_code': '603203', 'county': 'Kanchipuram', 'state_short': '25', 'state': 'Tamil Nadu', 'country': 'IN', 'city': 'Kavanur'}
        if sys.version_info[:2] <= (2, 7):
            self.assertItemsEqual(current_result, expected_result)
        else:
            self.assertCountEqual(current_result, expected_result)

    def test_ziptastic_valid_pincode_2(self):
        current_result = pz.query_ziptastic_api(94305, "US")
        expected_result = {'state_short': 'CA', 'state': 'California', 'city': 'Stanford', 'county': 'Santa Clara', 'country': 'US', 'postal_code': '94305'}
        if sys.version_info[:2] <= (2, 7):
            self.assertItemsEqual(current_result, expected_result)
        else:
            self.assertCountEqual(current_result, expected_result)

    def test_ziptastic_invalid_pincode(self):
        current_result = pz.query_ziptastic_api(33044)
        self.assertFalse(current_result)

    def test_googlemaps_valid_pincode(self):
        current_result = pz.query_google_api(603203, "IN")
        expected_result = {'bounds': {'northeast': {'lng': 80.0572497, 'lat': 12.8769479}, 'southwest': {'lng': 79.9504465, 'lat': 12.7997355}}, 'location_type': 'APPROXIMATE', 'location': {'lng': 80.0199562, 'lat': 12.8336666}}
        if sys.version_info[:2] <= (2, 7):
            self.assertItemsEqual(current_result, expected_result)
        else:
            self.assertCountEqual(current_result, expected_result)

    def test_get_valid_pincode(self):
        current_result = pz.get(603203, "IN")
        expected_result = {'state_short': '25', 'city': 'Kavanur', 'location': {'lat': 12.8336666, 'lng': 80.0199562}, 'state': 'Tamil Nadu', 'country': 'IN', 'postal_code': '603203', 'bounds': {'northeast': {'lat': 12.8769479, 'lng': 80.0572497}, 'southwest': {'lat': 12.7997355, 'lng': 79.9504465}}, 'county': 'Kanchipuram', 'location_type': 'APPROXIMATE'}
        if sys.version_info[:2] <= (2, 7):
            self.assertItemsEqual(current_result, expected_result)
        else:
            self.assertCountEqual(current_result, expected_result)        

    def test_get_invalid_pincode(self):
        current_result = pz.get(33044)
        self.assertFalse(current_result)

if __name__ == "__main__":
    unittest.main()