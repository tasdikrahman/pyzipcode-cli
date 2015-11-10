#!/usr/bin/env python
r"""
Usage:
  pyzipcode (ls | list)
  pyzipcode --p=PINCODE --c=COUNTRYCODE     
  pyzipcode --p=PINCODE 
  pyzipcode --version
  pyzipcode (-h | --help)
Options:
  -h --help     Show this screen
  -v --version  Show version  
"""


from docopt import docopt 
import os
import json
import requests

__version__ = '0.0.7'

country_file = 'countries.json' 
directory = os.path.dirname(os.path.abspath(__file__))
json_location = os.path.join(directory, country_file)

arguments = docopt(__doc__, version=__version__)

with open(json_location, 'r') as json_file:
    countries = json.loads(json_file.read())

def print_country_codes():
    '''prints all the countries with their respective country codes'''
    ## load the json file
    for k, v in countries.items():
        print('{key}      :  {key_value}'.format(key=k, key_value=v))


def make_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(response.json())
    else:
        print('something bad happened!')

def get_data():
    '''
    makes requests to the ziptest api in 
    the form of http://zip.getziptastic.com/v2/{country_code}/{pincode} 
    '''
    pincode = int(arguments['--p'])
    country_code = arguments['--c']
    ## make the requests
    url = 'http://zip.getziptastic.com/v2/{c}/{p}'.format(c=country_code, p=pincode)
    make_request(url)

def get_data_IN():
    '''
    If no country code is provided then the default country code is taken as "IN"
    requests will be made in the form of http://zip.getziptastic.com/v2/IN/{pincode} 
    '''
    pincode = int(arguments['--p'])
    url = 'http://zip.getziptastic.com/v2/IN/{p}'.format(p=pincode)
    make_request(url)

def main():
    '''pyzipcode is a simple API for Ziptest API v2. For more, do "pyzipcode --help"'''

    if arguments['ls'] or arguments['list']:
        print("Country : Country code")
        print("======= : ============")
        print_country_codes()

    elif arguments['--p'] and arguments['--c']:
        get_data()

    elif arguments['--p']:
        get_data_IN()
    
    elif arguments['--version'] or arguments['-v']:
        print(__version__)
    
    else:
        print(__doc__)

if __name__ == '__main__':
    main()