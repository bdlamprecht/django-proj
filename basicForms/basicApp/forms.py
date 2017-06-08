from django import forms
from django.core import validators

class MyForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    otheremail = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['otheremail']

        if email != vemail:
            raise forms.ValidationError("Ensure emails match")
