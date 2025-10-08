# forms.py
from django import forms
from .models import Customer,Student
from django.contrib import admin
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)




class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer       # ✅ specify which model this form is for
        fields = ['first_name', 'last_name']  # ✅ specify which fields to include



class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=["name","student_id","section","degree"]

