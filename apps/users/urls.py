from django.urls import path, include
from . import views

urlpatterns = [
    path('new', views.new_user),
    path('edit', views.edit_profile),
    path('edit/<int:user_id>', views.admin_edit_user),
    path('show/<int:user_id>', views.show_profile),
]