#!/usr/bin/env python
try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

setup(
  name = 'pyzipcode-cli',
  version = '0.0.8',
  author = 'Tasdik Rahman',
  author_email = 'tasdik95@gmail.com',
  packages = ['pyzipcode_cli'], 
  description = "a thin wrapper around getziptastic's API v2",
  url = 'https://github.com/prodicus/pyzipcode-cli', 
  license = 'MIT',
  install_requires = [
    "docopt==0.6.1",
    "requests==2.8.1"
  ],
  ## trying it with MANIFEST.in
  # include_package_data=True,
  # package_data={'pyzipcode_cli': ['*.json', 'pyzipcode_cli/countries.json']},
  download_url = 'https://github.com/prodicus/pyzipcode-cli/tarball/0.0.3', 
  classifiers = [
      'Intended Audience :: Developers',
      'Topic :: Software Development :: Build Tools',
      'License :: OSI Approved :: MIT License',

      # Specify the Python versions you support here. In particular, ensure
      # that you indicate whether you support Python 2, Python 3 or both.
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3.4',
  ],
  keywords = ['api', 'geo-location', 'zipcode','devtools', 'Development', 'ziptastic'], 
  entry_points = {
        'console_scripts': [
            'pyzipcode = pyzipcode_cli.core:main'
      ],
    }
)