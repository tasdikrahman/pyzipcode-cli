#!/usr/bin/env python
r"""
Usage:
  core.py (ls | list)  
  core.py (-h | --help)
  core.py --c=COUNTRY --p=PINCODE 
  core.py --p=pincode
  core.py --version
Options:
  -h --help     Show this screen
  -v --version  Show version  
"""


from docopt import docopt 
import os
import json


__version__ = '0.0.1'

root_dir = os.getcwd()
country_file = 'countries.json' 


with open('countries.json', 'r') as json_file:
    countries = json.loads(json_file.read())

def print_country_codes():
    '''prints all the countries with their respective country codes'''
    ## load the json file
    for k, v in countries.items():
        print('{key}      :  {key_value}'.format(key=k, key_value=v))


def get_data(country_code, pincode):
    '''
    makes requests to the ziptest api 
    in the form of http://zip.getziptastic.com/v2/{country_code}/{pincode}
    '''


def main():
    '''zipit is a simple API for Ziptest API v2. For more, do "zipit --help"'''
    
    arguments = docopt(__doc__, version=__version__)

    if arguments['ls'] or arguments['list']:
        print("Country : Country code")
        print("======= : ============")
        print_country_codes()
    
    elif arguments['--version'] or arguments['-v']:
        print(__version__)
    else:
        print(__doc__)

if __name__ == '__main__':
    main()