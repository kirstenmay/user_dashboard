from django.shortcuts import render
from login_reg.models import User

def index(request):
    return render(request, '/')
