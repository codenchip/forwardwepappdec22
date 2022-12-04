from helloworld import views
from django.urls import path

app_name = 'helloworld'

urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('dashboard/',views.dashboard,name='dashboard'),
]