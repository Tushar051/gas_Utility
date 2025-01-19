from django import forms
from .models import CustomerRequest

class CustomerRequestForm(forms.ModelForm):
    class Meta:
        model = CustomerRequest
        fields = [
            'customer_name',
            'customer_email',
            'customer_phone',
            'customer_address',
            'issue_description'
        ]
