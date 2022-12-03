pyvat -- VAT validation and calculation for Python
==================================================

.. image:: https://travis-ci.org/iconfinder/pyvat.png?branch=master
        :target: https://travis-ci.org/iconfinder/pyvat

With EU VAT handling rules becoming ever more ridiculous and complicated, businesses within the EU are faced with the complexity of having to validate VAT numbers. ``pyvat`` was built for `Iconfinder's marketplace <http://www.iconfinder.com/>`_ to handle just this problem.

Validation of VAT numbers is performed in two steps: firstly, the VAT number is checked against an expression for the given country if one such is available, after which it is checked against a registry if one such is available.

Calculation of VAT rates for sales is supported within the EU for items covered by the new EU directive for `VAT on telecommunications, broadcasting and electronic services <http://ec.europa.eu/taxation_customs/taxation/vat/how_vat_works/telecom/index_en.htm>`_.


Installation
------------

To install requests, do yourself a favor and don't use anything other than `pip <http://www.pip-installer.org/>`_:

.. code-block:: bash

    $ pip install pyvat


Usage
-----

``pyvat`` exposes its functionality through three simple methods:

``pyvat.check_vat_number(vat_number, country_code=None)``
   Test if a VAT number is valid.

   If possible, the VAT number will be checked against available registries.

   :Parameters:
      * ``vat_number`` -- VAT number to validate.
      * ``country_code`` -- Optional country code. Should be supplied if known, as there is no guarantee that naively entered VAT numbers contain the correct alpha-2 country code prefix for EU countries just as not all non-EU countries have a reliable country code prefix. Default ``None`` prompting detection.

   :Returns:
      ``True`` if the VAT number can be fully asserted as valid or ``False`` if not, otherwise ``None`` indicating that the VAT number may or may not be valid.


``pyvat.is_vat_number_format_valid(vat_number, country_code=None)``
   Test if the format of a VAT number is valid.

   :Parameters:
      * ``vat_number`` -- VAT number to validate.
      * ``country_code`` -- Optional country code. Should be supplied if known, as there is no guarantee that naively entered VAT numbers contain the correct alpha-2 country code prefix for EU countries just as not all non-EU countries have a reliable country code prefix. Default ``None`` prompting detection.

   :Returns:
      ``True`` if the VAT number can be fully asserted as valid or ``False`` if not, otherwise ``None`` indicating that the VAT number may or may not be valid.


``pyvat.get_sale_vat_charge(date, item_type, buyer, seller)``
   Get the VAT charge for performing the sale of an item.

   Currently only supports determination of the VAT charge for
   telecommunications, broadcasting and electronic services in the EU.

   :Parameters:
      * ``date`` (``datetime.date``) -- Sale date.
      * ``item_type`` (``pyvat.ItemType``) -- Type of the item being sold.
      * ``buyer`` (``pyvat.Party``) -- Buyer.
      * ``seller`` (``pyvat.Party``) -- Seller.

   :Returns:
      The VAT charge to be applied to the sale of an item.


For more detailed documentation, see the `full pyvat documentation <http://pyvat.readthedocs.org/>`_.
