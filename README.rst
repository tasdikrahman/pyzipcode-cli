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

by just using the ``ZIPCODE`` and `Country code <https://github.com/tasdikrahman/pyzipcode-cli/wiki/Countries-ISO-Codes>`__

Features
--------

-  Written in uncomplicated ``python``
-  Supports all the Country codes specified in the ISO specification i.e
   all **264 countries** where they have a pin code.

   You can find a list of all the country codes at `the Wiki page <https://github.com/tasdikrahman/pyzipcode-cli/wiki/Countries-ISO-Codes>`__
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

    $ git clone https://github.com/tasdikrahman/pyzipcode-cli.git
    $ cd pyzipcode-cli/
    $ pip install -r requirements.txt
    $ python setup.py install

Usage
-----

``get()``
~~~~~~~~~

.. code:: bash

    >>> from pyzipcode import Pyzipcode as pz
    >>> pz.get(603203, "IN", return_json=True)
    {
      "location": {
        "lat": 12.8336666,
        "lng": 80.0199562
      },
      "city": "Kavanur",
      "state_short": "25",
      "county": "Kanchipuram",
      "state": "Tamil Nadu",
      "postal_code": "603203",
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
      "location_type": "APPROXIMATE",
      "country": "IN"
    }

    >>>
    >>> pz.get(94305, "US", return_json=True)
    {
      "city": "Stanford",
      "country": "US",
      "bounds": {
        "northeast": {
          "lat": 37.44363,
          "lng": -122.1494501
        },
        "southwest": {
          "lat": 37.382743,
          "lng": -122.194849
        }
      },
      "county": "Santa Clara",
      "state": "California",
      "state_short": "CA",
      "postal_code": "94305",
      "location": {
        "lat": 37.4135757,
        "lng": -122.1689284
      },
      "location_type": "APPROXIMATE"
    }


To-do
-----

-  [ ] Support ``timezone`` extraction
-  [ ] Add cli-support

Contributing
------------

Feel free to make a pull request. For that, please refer the `Contributing page <https://github.com/tasdikrahman/pyzipcode-cli/blob/master/CONTRIBUTING.rst>`__ 

Bugs
----

Please report the bugs at the `issue
tracker <https://github.com/tasdikrahman/pyzipcode-cli/issues>`__

Known Issues
------------

-   The zipcodes for Argentina are not working for the release `0.1.3 <https://github.com/tasdikrahman/pyzipcode-cli/releases/tag/v0.1.3>`__ as reported by `DavidVentura <https://github.com/DavidVentura>`__ on issue `#1 <https://github.com/tasdikrahman/pyzipcode-cli/issues/1>`__

License :
---------

`MIT License <http://prodicus.mit-license.org/>`__ © `Tasdik Rahman <https://tasdikrahmans.com/>`__

You can find a copy of the License at http://prodicus.mit-license.org/

Donation
--------

If you have found my little bits of software being of any use to you, do consider helping me pay my internet bills :)


|Paypal badge|

|Instamojo|

|gratipay|

|patreon|


.. |PyPI version| image:: https://badge.fury.io/py/pyzipcode-cli.svg
   :target: https://badge.fury.io/py/pyzipcode-cli
.. |License| image:: https://img.shields.io/pypi/l/pyzipcode-cli.svg
   :target: https://img.shields.io/pypi/l/pyzipcode-cli.svg
.. |Python Versions| image:: https://img.shields.io/pypi/pyversions/pyzipcode-cli.svg
.. |Build Status| image:: https://travis-ci.org/tasdikrahman/pyzipcode-cli.svg?branch=master
.. |Requirements Status| image:: https://requires.io/github/tasdikrahman/pyzipcode-cli/requirements.svg?branch=master
   :target: https://requires.io/github/tasdikrahman/pyzipcode-cli/requirements/?branch=master
   :alt: Requirements Status
.. |Paypal badge| image:: https://www.paypalobjects.com/webstatic/mktg/logo/AM_mc_vs_dc_ae.jpg
   :target: https://www.paypal.me/tasdik
.. |gratipay| image:: https://cdn.rawgit.com/gratipay/gratipay-badge/2.3.0/dist/gratipay.png
   :target: https://gratipay.com/tasdikrahman/
.. |Instamojo| image:: https://www.soldermall.com/images/pic-online-payment.jpg
   :target: https://www.instamojo.com/@tasdikrahman
.. |patreon| image:: http://i.imgur.com/ICWPFOs.png
   :target: https://www.patreon.com/tasdikrahman/
