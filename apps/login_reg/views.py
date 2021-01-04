from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt
import datetime


def login_reg(request):
    return render(request, 'register.html')

def register(request):
    errors = User.objects.reg_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/')
    else:
        users = User.objects.all()
        if len(users) == 0:
            userLevel = "admin"
        else:
            userLevel = "normal"
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], birthday = request.POST['birthday'], email = request.POST['email'], password = pw_hash, user_level = userLevel)
        request.session['userid'] = new_user.id
        username = new_user.first_name
        request.session['username'] = username
        if new_user.user_level == "admin":
            return redirect('/dashboard/admin')
        return redirect('/dashboard/')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/")
    else:
        user = User.objects.filter(email = request.POST['login_email'])
        logged_user = user[0]
        request.session['userid'] = logged_user.id
        username = logged_user.first_name
        request.session['username'] = username
        if logged_user.user_level == "admin":
            return redirect('/dashboard/admin')
        return redirect('/dashboard/')

def log_out(request):
    request.session.clear()
    return redirect("/")
