from django.utils.translation import ugettext_lazy as _
from django.db.models.fields import CharField


class ZipCodeField(CharField):

    description = _("Thai postal code")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 5
        super(ZipCodeField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        from django_localflavor_th.forms import THZipCodeField
        defaults = {'form_class': THZipCodeField}
        defaults.update(kwargs)
        return super(ZipCodeField, self).formfield(**defaults)


class PhoneNumberField(CharField):

    description = _("Phone number")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 20
        super(PhoneNumberField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        from django_localflavor_th.forms import THPhoneNumberField
        defaults = {'form_class': THPhoneNumberField}
        defaults.update(kwargs)
        return super(PhoneNumberField, self).formfield(**defaults)

# TODO:  models.THZipCodeField: needed to be implemented.
