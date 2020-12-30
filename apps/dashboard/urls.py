from django.urls import path, include
from . import views

urlpatterns = [
    path('admin', views.admin_dashboard),
    path('', views.dashboard)
]