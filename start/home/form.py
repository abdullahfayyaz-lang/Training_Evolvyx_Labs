# forms.py
from django import forms
from .models import Customer
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)




class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer       # ✅ specify which model this form is for
        fields = ['first_name', 'last_name']  # ✅ specify which fields to include


