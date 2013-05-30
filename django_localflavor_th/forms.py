"""
Thailand-specific Form helpers
"""

from __future__ import absolute_import, unicode_literals

import re

from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.forms.fields import Field, RegexField, Select, CharField
from django.utils.encoding import smart_text
from django.utils.translation import ugettext_lazy as _

phone_digits_re = re.compile(r'^(?:1-?)?(\d{3})[-\.]?(\d{3})[-\.]?(\d{4})$')

mobile_digits_re = re.compile(r'^(0)?(\d{2})[-\.]?(\d{3})[-\.]?(\d{4})$')
metro_phone_digits_re = re.compile(r'^(?:0-?)?(2)[-\.]?(\d{3})[-\.]?(\d{4})$')
non_metro_phone_digits_re = re.compile(r'^0?(\d{2})[-\.]?(\d{3})[-\.]?(\d{3})$')


# TODO: forms.THProvinceField: needed to be implemented.

class THPhoneNumberField(CharField):
    default_error_messages = {
        'invalid':  _('Phone numbers must be in correct formats.'),
    }

    def clean(self, value):
        super(THPhoneNumberField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''
        value = re.sub('(\(|\)|\s+)', '', smart_text(value))
        if mobile_digits_re.search(value):
            return '0%s-%s-%s' % (m.group(1), m.group(2), m.group(3))
        elif metro_phone_digits_re.search(value):
            return '02-%s-%s' % (m.group(1), m.group(2))
        elif non_metro_phone_digits_re.search(value):
            return '0%s-%s-%s' % (m.group(1), m.group(2), m.group(3))
        raise ValidationError(self.default_error_messages['invalid'])


class THZipCodeField(RegexField):
    
    """
       checking if the value is in correct form.
    """
    default_error_messages = {
        'invalid': _('Enter a zip code in the format XXXXX.'),
    }

    def __init__(self, max_length=None, min_length=None, *args, **kwargs):
        super(THZipCodeField, self).__init__(r'^\d{5}$',
            max_length, min_length, *args, **kwargs)


class THNationalIdField(Field):
    """
    There is a last digit for checking if it's correct Thai national ID,
    that's what we do here.
    """
    default_error_messages = {
        'invalid': _('Enter a valid Thai natioal ID in X-XXXX-XXXXX-XX-X format.'),
        'incompleted': _('Enter 13-digit number.'),
    }

    def clean(self, value):
        super(THNationalIdField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''

        # check if it is only number
        if not re.search(r'^\d+$', value):
            raise ValidationError(self.default_error_messages['invalid'])

        # number has to have exact 13 digit
        if len(value) is not 13:
            raise ValidationError(self.default_error_messages['invalid'])

        # check integrity of people_id
        v = value
        sum = int(v[:1]) * 13 + int(v[1:2]) * 12 + int(v[2:3]) * 11 \
            + int(v[3:4]) * 10 + int(v[4:5]) * 9 + int(v[5:6]) * 8 \
            + int(v[6:7]) * 7 + int(v[7:8]) * 6 + int(v[8:9]) * 5 \
            + int(v[9:10]) * 4 + int(v[10:11]) * 3 + int(v[11:12]) * 2
        sum = 11 - sum % 11
        if sum > 9:
            sum = sum - 10
        if sum != int(v[12:13]):
            raise ValidationError(self.default_error_messages['invalid'])

        return '%s-%s-%s-%s-%s' % (v[:1], v[1:5], v[5:10], v[10:12], v[12:13])
