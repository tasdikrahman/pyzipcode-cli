#!/usr/bin/env python
r"""
Usage:
  core.py (ls | list)  
  core.py --p=PINCODE --c=COUNTRY     
  core.py --p=PINCODE                   ## default --c: IN
  core.py --version
  core.py (-h | --help)
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


def get_data():
    '''
    makes requests to the ziptest api in 
    the form of http://zip.getziptastic.com/v2/{country_code}/{pincode} 
    '''
    pass


def get_data_IN():
    '''
    If no country code is provided then the default country code is taken as "IN"
    requests will be made in the form of http://zip.getziptastic.com/v2/IN/{pincode} 
    '''
    pass


def main():
    '''zipit is a simple API for Ziptest API v2. For more, do "zipit --help"'''
    
    arguments = docopt(__doc__, version=__version__)

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