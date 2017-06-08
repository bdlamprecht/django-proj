from django import forms
from my2ndApp.models import MyUser

class NewUserForm(forms.ModelForm):
    class Meta():
        model = MyUser
        fields = '__all__'
