from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['title', 'first_name', 'last_name', 'phone_number', 'email']
