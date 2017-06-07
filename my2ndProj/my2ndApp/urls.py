from django.conf.urls import url
from my2ndApp import views

urlpatterns = [
    url(r'^$',views.users,name='users')
]
