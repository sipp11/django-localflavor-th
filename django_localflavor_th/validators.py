# -*- coding: utf-8 -*-

import re
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from datetime import date


# from django.core.validators import RegexValidator

class THNationalIdValidator(object):

    message = _('Enter a valid value.')
    code = 'invalid'

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):

        # check if it is only number

        if not re.search(r'^\d+$', value):
            raise ValidationError(_('Enter only numbers.'), self.code)

        # number has to have exact 13 digit

        if len(value) is not 13:
            raise ValidationError(_('Enter 13-digit number.'),
                                  self.code)

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
            raise ValidationError(self.message, self.code)


validate_people_id = THNationalIdValidator()
