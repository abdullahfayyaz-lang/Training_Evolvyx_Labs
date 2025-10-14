from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User  # Custom user model

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        def clean_email(self):
            email=self.cleaned_data.get('email')
            if '@example.com' not in email:
                raise forms.ValidationError('Invalid Email Domain .')
            return email