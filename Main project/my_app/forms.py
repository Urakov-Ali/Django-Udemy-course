from turtle import textinput
from django import forms

class OrderForm(forms.Form):
    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class':'form-control'}))
