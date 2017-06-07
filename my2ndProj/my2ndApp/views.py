from django.shortcuts import render
from my2ndApp.models import MyUser

# Create your views here.
def index(request):
    return render(request,'my2ndApp/index.html')

def users(request):
    user_list = MyUser.objects.order_by('fName')
    user_dict = {'users':user_list}
    return render(request,'my2ndApp/users.html',context=user_dict)
