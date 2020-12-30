from django.shortcuts import render, redirect
from apps.login_reg.models import User

def new_user(request):
    if 'userid' in request.session:
        return render(request, 'new_user.html')
    else:
        return redirect('/')

def create_user(request):
    pass

def edit_profile(request):
    if 'userid' in request.session:
        return render(request, 'edit_profile.html')
    else:
        return redirect('/')

def change_profile(request):
    #should be able to get user from session here
    pass

def admin_edit_user(request, user_id):
    if 'userid' in request.session:
        return render(request, 'admin_edit.html')
    else:
        return redirect('/')

def admin_change_user(request):
    pass

def show_profile(request, user_id):
    if 'userid' in request.session:
        return render(request, 'show_users.html')
    else:
        return redirect('/')

def create_message(request):
    pass

def create_comment(request):
    pass



