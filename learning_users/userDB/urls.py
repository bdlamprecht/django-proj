from django.conf.urls import url
from userDB import views

app_name='userDB'

urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$',views.user_login,name='user_login')
]
