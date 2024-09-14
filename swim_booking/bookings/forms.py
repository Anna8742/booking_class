from django import forms
from django.contrib.auth.models import User
from .models import Parent, Child, Booking

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['name', 'date_of_birth']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['child', 'swim_class']
