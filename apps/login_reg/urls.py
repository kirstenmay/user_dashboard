from django.urls import path, include
from . import views
                    
urlpatterns = [
    path('log_out', views.log_out),
    path('login', views.login),
    path('register', views.register),
    path('', views.login_reg),
]
