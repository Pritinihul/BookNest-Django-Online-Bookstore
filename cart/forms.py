from django import forms
from .models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'full_Name',
            'address',
            'contact',
            'State',
            'city',
            'pincode',
        ]