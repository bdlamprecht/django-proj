from django import forms
from django.core import validators

class MyForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botc = forms.CharField(required=False,
                          widget=forms.HiddenInput,
                          validators=[validators.MaxLengthValidator(0)])
