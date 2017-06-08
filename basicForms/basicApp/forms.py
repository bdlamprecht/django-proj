from django import forms

class MyForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botc = forms.CharField(required=False,
                          widget=forms.HiddenInput)

    def clean_botc(self):
        botc = self.cleaned_data['botc']
        if len(botc) > 0:
            raise forms.ValidationError("GOTCHA")
        return botc
