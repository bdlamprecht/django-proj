from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
        return render(request,'basicApp/index.html')

def form_name_view(request):
    theForm = forms.MyForm()

    if request.method == 'POST':
        theForm = forms.MyForm(request.POST)

        if theForm.is_valid():
            print("VALIDATION SUCCESS!")
            print("Name:  "+theForm.cleaned_data['name'])
            print("Email: "+theForm.cleaned_data['email'])
            print("Text:  "+theForm.cleaned_data['text'])

    return render(request,'basicApp/form_page.html',{'form':theForm})
