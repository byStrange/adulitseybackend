# import forms
from django import forms
from . import models

# form for rector contact


class RectorContactForm(forms.ModelForm):
    class Meta:
        model = models.RectorContact
        fields = [
            'summary',
            'text',
            'name',
            'surname',
            'last_name',
            'phone_num_or_username',
            'address',
            'status',
            'contact_type'
        ]

# form for anonymous contact


class AnonymousContactForm(forms.ModelForm):
    class Meta:
        model = models.AnonymousContact
        fields = [
            'text',
            'name',
            'phone_num_or_username',
            'email'
        ]
