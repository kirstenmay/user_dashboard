from django.shortcuts import render, redirect
from apps.login_reg.models import User
from django.contrib import messages
import bcrypt

def new_user(request):
    if 'userid' in request.session:
        user = User.objects.get(id=int(request.session['userid']))
        if user.user_level != 'admin':
            return redirect('/dashboard/')
        else:
            return render(request, 'new_user.html')
    else:
        return redirect('/')

def create_user(request):
    errors = User.objects.reg_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/users/new/")
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        userLevel = 'normal'
        User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], birthday = request.POST['birthday'], email = request.POST['email'], password = pw_hash, user_level = userLevel)
        return redirect('/dashboard/admin')

def edit_profile(request):
    if 'userid' in request.session:
        user = User.objects.get(id=int(request.session['userid']))
        context = {
            'user': user
        }
        return render(request, 'edit_profile.html', context)
    else:
        return redirect('/')

def change_profile(request):
    user = User.objects.get(id=int(request.POST['user']))
    errors = User.objects.reg_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/users/edit/")
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.birthday = request.POST['birthday']
        user.email = request.POST['email']
        user.password = pw_hash
        user.save()
        return redirect('/dashboard/')

def admin_edit_user(request, user_id):
    if 'userid' in request.session:
        user = User.objects.get(id=int(request.session['userid']))
        if user.user_level != 'admin' or user.id == user_id:
            return render(request, 'edit_profile.html')
        else:
            context = {
                'user': user
            }
            return render(request, 'admin_edit.html', context)
    else:
        return redirect('/')

def admin_change_user(request):
    user = User.objects.get(id=int(request.POST['user']))
    logged_in_user = User.objects.get(id=int(request.session['userid']))
    if logged_in_user.user_level != 'admin':
        return redirect('/dashboard/')
    else:
        errors = User.objects.reg_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect(f"/users/edit/{user.id}")
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.birthday = request.POST['birthday']
            user.email = request.POST['email']
            user.password = pw_hash
            user.user_level = request.POST['user_level']
            user.save()
            return redirect('/dashboard/admin/')

def show_profile(request, user_id):
    if 'userid' in request.session:
        user = User.objects.get(id=user_id)
        context = {
            'user': user
        }
        return render(request, 'show_users.html', context)
    else:
        return redirect('/')

def create_message(request):
    pass

def create_comment(request):
    pass



