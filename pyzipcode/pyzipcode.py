#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
try:
    import json
except ImportError:
    import simplejson as json


__version__ = '0.1.2'
__author__ = "Tasdik Rahman"


class Pyzipcode(object):

    BASE_URL_ZIPTASTIC_API = 'http://zip.getziptastic.com/v2/{code}/{pin}'
    BASE_URL_GOOGLE_API = 'http://maps.googleapis.com/maps/api/geocode/json?address={pin}'

    @staticmethod
    def query_ziptastic_api(pincode, country_code="IN", return_json=False):
        """
        appends the pincode to the base API url and queries the API.
        country_code defaults to 'IN'

        :param pincode: The pincode 
        :param country_code: The country for the pincode. Defaults to "IN"
        :returns: returns the JSON data returned by the API
        """
        
        url = Pyzipcode.BASE_URL_ZIPTASTIC_API.format(code=country_code, pin=pincode)
        response = requests.get(url)
        if response.status_code == 200:
            json_obj = response.json()
            if return_json == True:
                return json.dumps(json_obj)
            else:
                return json_obj
        else:
            return False


    @staticmethod
    def query_google_api(pincode, return_json=False):
        """
        queries the Google maps API for getting the longitude and latitude 
        for a given pincode

        :param pincode: The pincode
        :returns: returns the latitude and longitude
        """

        url = Pyzipcode.BASE_URL_GOOGLE_API.format(pin=pincode)
        response = requests.get(url)
        if response.status_code == 200:
            json_obj = response.json()
            if json_obj["status"] == "OK":
                results = json_obj["results"][0]["geometry"]
                
                '''Storing the JSON data'''
                data = {
                    "location": results["location"],   
                    "location_type": results["location_type"],
                    "bounds": results["bounds"]
                }
                if return_json == True:
                    return json.dumps(data)
                else:
                    return data
            else:
                return False
        else:
            return False


    @staticmethod
    def get_data(pincode, country_code="IN",return_json=False):
        """
        Unifies the JSON data from different API's into a single one

        :param pincode: pincode for the place
        :param country_code: country code for the pincode. You can find the list of country codes in 
                             "https://github.com/prodicus/pyzipcode-cli/blob/master/pyzipcode_cli/countries.json"
        :returns: A unified result of both ziptastic and google maps API
        """

        data_API_1 = Pyzipcode.query_ziptastic_api(pincode, country_code)
        data_API_2 = Pyzipcode.query_google_api(pincode)

        if data_API_2 is not False and data_API_1 is not False:
            final_dictionary = { 
                "ziptastic": data_API_1,
                "google_maps": data_API_2
            }
            if return_json == True:
                return json.dumps(final_dictionary)
            else:
                return final_dictionary
        else:
            return False