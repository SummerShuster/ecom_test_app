from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(label="Full Name", widget=forms.TextInput(attrs={'class': 'form-control', 'Full Name': 'Phone'}),required=True)
    shipping_email = forms.CharField(label="Email",widget=forms.TextInput(attrs={'class': 'form-control', 'Email Address': 'Phone'}),required=True)
    shipping_address1 = forms.CharField(label="Shipping Address 1",widget=forms.TextInput(attrs={'class': 'form-control', 'Address 1': 'Phone'}),required=True)
    shipping_address2 = forms.CharField(label="Shipping Address 2",widget=forms.TextInput(attrs={'class': 'form-control', 'Address 2': 'Phone'}),required=False)
    shipping_city = forms.CharField(label="City",widget=forms.TextInput(attrs={'class': 'form-control', 'City': 'Phone'}),required=True)
    shipping_state = forms.CharField(label="State",widget=forms.TextInput(attrs={'class': 'form-control', 'State': 'Phone'}),required=False)
    shipping_zipcode = forms.CharField(label="Zipcode",widget=forms.TextInput(attrs={'class': 'form-control', 'Zipcode': 'Phone'}),required=False)
    shipping_country = forms.CharField(label="Country",widget=forms.TextInput(attrs={'class': 'form-control', 'Country': 'Phone'}),required=True)

    class Meta:
        model = ShippingAddress
        fields = ['shipping_full_name','shipping_email','shipping_address1','shipping_address2','shipping_city','shipping_state','shipping_zipcode','shipping_country']
        exclude = ['user',]

from django import forms


class PaymentForm(forms.Form):
    card_name = forms.CharField(
        label="Name on Card",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Name on Card'
        }),
        required=True
    )

    card_number = forms.CharField(
        label="Card Number",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '1234 5678 9012 3456'
        }),
        required=True
    )

    card_exp_date = forms.CharField(
        label="Expiration Date",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'MM/YY'
        }),
        required=True
    )

    card_cvv_number = forms.CharField(
        label="CVV",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'CVV'
        }),
        required=True
    )

    card_address1 = forms.CharField(
        label="Billing Address 1",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Street Address'
        }),
        required=True
    )

    card_address2 = forms.CharField(
        label="Billing Address 2",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Apartment, Suite, etc. (optional)'
        }),
        required=False
    )

    card_city = forms.CharField(
        label="City",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'City'
        }),
        required=True
    )

    card_state = forms.CharField(
        label="State",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'State'
        }),
        required=True
    )

    card_zipcode = forms.CharField(
        label="Zip Code",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Zip Code'
        }),
        required=True
    )

    card_country = forms.CharField(
        label="Country",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Country'
        }),
        required=True
    )
