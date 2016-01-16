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

by just using the ``ZIPCODE`` and `Country code <https://github.com/prodicus/pyzipcode-cli/wiki/Countries-ISO-Codes>`__

Features
--------

-  Written in uncomplicated ``python``
-  Supports all the Country codes specified in the ISO specification i.e
   all **264 countries** where they have a pin code.

   You can find a list of all the country codes at `the Wiki page <https://github.com/prodicus/pyzipcode-cli/wiki/Countries-ISO-Codes>`__
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

.. figure:: https://raw.githubusercontent.com/prodicus/pyzipcode-cli/master/assets/pyzip_demo.gif
   :alt: Demp link

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
      "postal_code": "603203",
      "county": "Kanchipuram",
      "state_short": "25",
      "location": {
        "lat": 12.8336666,
        "lng": 80.0199562
      },
      "state": "Tamil Nadu",
      "location_type": "APPROXIMATE",
      "bounds": {
        "northeast": {
          "lat": 12.8769479,
          "lng": 80.0572497
        },
        "southwest": {
          "lat": 12.7997355,
          "lng": 79.9504465
        }
      },
      "city": "Kavanur",
      "country": "IN"
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

Known Issues
------------

-   The zipcodes for Argentina are not working for the release `0.1.3 <https://github.com/prodicus/pyzipcode-cli/releases/tag/v0.1.3>`__ as reported by `DavidVentura <https://github.com/DavidVentura>`__ on issue `#1 <https://github.com/prodicus/pyzipcode-cli/issues/1>`__

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