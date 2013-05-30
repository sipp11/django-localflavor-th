=====================
django_localflavor_th
=====================

Country-specific Django helpers for Thailand

What's in Thailand localflavor?
=================================

* forms.THPhoneNumberField: A form field that validates input as a Thai 
  phone number which we have multiple formats
    * Mobile phone: XXX-XXX-XXXX
    * Metro area landline: X-XXXX-XXXX
    * Outside metro area landline: XXX-XXX-XXX


* forms.THZipCodeField: A form field that validates input as a Thai ZIP code.
  Valid formats are XXXXX.


* forms.THNationalIdField: A form field that validates input as an ID
  number which obeys some rules
    * Format X-XXXX-XXXXX-XX-X
    * last digit was a check bit


## TODO yet to implement


* forms.THProvinceField: A form field that validates input as a province in
  Thailand.


* models.THProvinceField: A model field that forms represent as a
  ``forms.THProvinceield``

* models.THPostalCodeField: A model field that forms represent as a
  ``forms.THPSSelect``

