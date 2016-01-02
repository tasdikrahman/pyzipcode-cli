Pyzipcode
=========

|PyPI version| |License| |Python Versions| |Build Status| |Requirements Status|

:Author: Tasdik Rahman

.. contents::
    :backlinks: none

.. sectnum::

What is it?
-----------

Extract meta data like 

-  ``city``
-  ``state``
-  ``county``
-  ``location``

   -  ``latitude``
   -  ``longitude``

-  Appropriate boundaries for that area

by just using the ``ZIPCODE`` and `Country code <https://github.com/prodicus/pyzipcode-cli/blob/master/assets/countries.json>>`__

Features
--------

-  Written in uncomplicated ``python``
-  Supports all the Country codes specified in the ISO specification i.e
   all **264 countries** where they have a pin code.

   You can find a list of all the country codes at `countries.json <https://github.com/prodicus/pyzipcode-cli/blob/master/assets/countries.json>`__
-  Gives ouput in a ``dict`` form or a ``JSON`` format
-  Fast and easy to use


Installation
------------

Option 1: installing through `pip <https://pypi.python.org/pypi/pyzipcode-cli>`__ (Suggested way)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`pypi package link <https://pypi.python.org/pypi/pyzipcode-cli>`__

``$ pip install pyzipcode-cli``

If you are behind a proxy

``$ pip --proxy [username:password@]domain_name:port install pyzipcode-cli``

**Note:** If you get ``command not found`` then
``$ sudo apt-get install python-pip`` should fix that

Option 2: Installing from source
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    $ git clone https://github.com/prodicus/pyzipcode-cli.git
    $ cd pyzipcode-cli/
    $ pip install -r requirements.txt
    $ python setup.py install

Usage
-----

``query_ziptastic_api()``
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    >>> from pyzipcode import Pyzipcode as pz
    >>> pz.query_ziptastic_api(603203, "IN")
    {
      "state_short": "25",
      "state": "Tamil Nadu",
      "county": "Kanchipuram",
      "postal_code": "603203",
      "city": "Kavanur",
      "country": "IN"
    }
    >>>

``query_google_api()``
~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    >>> pz.query_google_api(603203, "IN")
    {
      "location_type": "APPROXIMATE",
      "location": {
        "lng": 80.0199562,
        "lat": 12.8336666
      },
      "bounds": {
        "northeast": {
          "lng": 80.0572497,
          "lat": 12.8769479
        },
        "southwest": {
          "lng": 79.9504465,
          "lat": 12.7997355
        }
      }
    }

``get_data()``
~~~~~~~~~~~~~~

.. code:: bash

    >>> pz.get_data(94305, "US")
    {
      "google_maps": {
        "location_type": "APPROXIMATE",
        "location": {
          "lng": -122.1689284,
          "lat": 37.4135757
        },
        "bounds": {
          "northeast": {
            "lng": -122.1494501,
            "lat": 37.44363
          },
          "southwest": {
            "lng": -122.194849,
            "lat": 37.382743
          }
        }
      },
      "ziptastic": {
        "city": "Stanford",
        "state": "California",
        "postal_code": "94305",
        "state_short": "CA",
        "county": "Santa Clara",
        "country": "US"
      }
    }

To-do
-----

-  [ ] Support ``timezone`` extraction
-  [ ] Add cli-support

Contributing
------------

Feel free to make a pull request. For that, please refer the `Contributing page <https://github.com/prodicus/pyzipcode-cli/blob/master/CONTRIBUTING.rst>`__ 

Bugs
----

Please report the bugs at the `issue
tracker <https://github.com/prodicus/pyzipcode-cli/issues>`__

License :
---------

`MIT License <http://prodicus.mit-license.org/>`__ © `Tasdik Rahman <http://prodicus.github.com/>`__

You can find a copy of the License at http://prodicus.mit-license.org/

.. |PyPI version| image:: https://badge.fury.io/py/pyzipcode-cli.svg
   :target: https://badge.fury.io/py/pyzipcode-cli
.. |License| image:: https://img.shields.io/pypi/l/pyzipcode-cli.svg
   :target: https://img.shields.io/pypi/l/pyzipcode-cli.svg
.. |Python Versions| image:: https://img.shields.io/pypi/pyversions/pyzipcode-cli.svg
.. |Build Status| image:: https://travis-ci.org/prodicus/pyzipcode-cli.svg?branch=master
.. |Requirements Status| image:: https://requires.io/github/prodicus/pyzipcode-cli/requirements.svg?branch=master
   :target: https://requires.io/github/prodicus/pyzipcode-cli/requirements/?branch=master
   :alt: Requirements Status