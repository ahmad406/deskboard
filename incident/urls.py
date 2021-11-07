from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name='home'),
    path('login', views.login,name='login'),
    path('incident', views.incident,name='incident'),
    path('register', views.register,name='register'),
    path("logout",views.login,name='logout'),
  
]

