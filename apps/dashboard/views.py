from django.shortcuts import render, redirect
from apps.login_reg.models import User

def admin_dashboard(request):
    if 'userid' in request.session:
        return render(request, 'admin_dashboard.html')
    else:
        return redirect('/')

def dashboard(request):
    if 'userid' in request.session:
        return render(request, 'dashboard.html')
    else:
        return redirect('/')
