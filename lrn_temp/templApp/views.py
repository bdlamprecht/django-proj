from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'templApp/index.html')

def other(request):
    return render(request,'templApp/other.html')

def relative(request):
    return render(request,'templApp/relative_url_templates.html')
