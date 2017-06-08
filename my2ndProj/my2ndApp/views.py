from django.shortcuts import render
from my2ndApp.forms import NewUserForm

# Create your views here.
def index(request):
    return render(request,'my2ndApp/index.html')

def users(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error form invalid!")

    return render(request,'my2ndApp/users.html',{'form':form})
