##pyzipcode-cli

[![PyPI version](https://badge.fury.io/py/pyzipcode-cli.svg)](https://badge.fury.io/py/pyzipcode-cli) [![License](https://img.shields.io/pypi/l/pyzipcode-cli.svg)](https://img.shields.io/pypi/l/pyzipcode-cli.svg) 

pyzipcode-cli is a thin wrapper around getziptastic's API v2

##Demo

![Usage](https://raw.githubusercontent.com/prodicus/pyzipcode-cli/master/usage.gif)

##Features

- Supports all the Country codes specified in the ISO specification i.e all **264 countries** where they have a pin code.
- Gives ouput in `JSON` format.
- A clean command line interface which abides with `POSIX` interface.
- written in python
- works on Mac, Linux, Windows

##Installation

##Option 1: installing from source

```bash
$ git clone https://github.com/prodicus/pyzipcode-cli.git
$ cd pyzipcode-cli/pyzipcode-cli
$ python setup.py install
```

##Option 2: installing through [pip](https://pypi.python.org/pypi/pyzipcode-cli)

[pypi package link](https://pypi.python.org/pypi/pyzipcode-cli)

`$ pip install pyzipcode-cli`

##Usage

```bash
$ pyzipcode --p=248001 --c=IN
{'county': 'Dehradun', 'country': 'IN', 'postal_code': '248001', 'state_short': '39', 'city': 'Kanwali', 'state': 'Uttarakhand'}
```

If you don't specify the option `--c`, country code will default as `IN` and `pyzipcode` will try to search for the particular zipcode in `India`

```bash
$ pyzipcode --p=603203 
{'postal_code': '603203', 'city': 'Kavanur', 'state': 'Tamil Nadu', 'county': 'Kanchipuram', 'state_short': '25', 'country': 'IN'}
```

```bash
$ pyzipcode --p=48867 --c=US
{'county': 'Shiawassee', 'city': 'Owosso', 'country': 'US', 'postal_code': '48867', 'state': 'Michigan', 'state_short': 'MI'}
```

####Get list of all countries with their country codes

`$ pyzipcode ls` 

You can search for a country by piping it 

```bash
$ ./pyzipcode.py ls | grep kistan
PK      :  Pakistan
UZ      :  Uzbekistan
TJ      :  Tajikistan
$
```
####Version

```bash
$ pyzipcode -v
0.0.1
$
```

####Help

```bash
$ pyzipcode --help
Usage:
  pyzip.py (ls | list)
  pyzip.py --p=PINCODE --c=COUNTRYCODE     
  pyzip.py --p=PINCODE 
  pyzip.py --version
  pyzip.py (-h | --help)
Options:
  -h --help     Show this screen
  -v --version  Show version  
$
```

##To-do

- [ ] Add support for calculating distance between two cities
- [ ] adding details like
    - [ ] Longitude and Latitude
    - [ ] Time zone

##Contributing

Feel free to contribute

1. Fork it.
2. Create your feature branch (`git checkout -b my-new-awesome-feature`)
3. Commit your changes (`git commit -am 'Added <xyz> feature'`)
4. Push to the branch (`git push origin my-new-awesome-feature`)
5. Create new Pull Request

##Bugs

Please report the bugs at the [issue tracker](https://github.com/prodicus/pyzipcode-cli/issues)

## License :

MIT License [http://prodicus.mit-license.org/](http://prodicus.mit-license.org/) &copy; Tasdik Rahman
