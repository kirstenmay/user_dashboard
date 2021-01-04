from django.shortcuts import render, redirect
from apps.login_reg.models import User

def admin_dashboard(request):
    if 'userid' in request.session:
        user = User.objects.get(id=int(request.session['userid']))
        if user.user_level != 'admin':
            return render(request, 'dashboard.html')
        else:
            context = {
                'users': User.objects.all()
            }
            return render(request, 'admin_dashboard.html', context)
    else:
        return redirect('/')

def dashboard(request):
    if 'userid' in request.session:
        context = {
                'users': User.objects.all()
            }
        return render(request, 'dashboard.html', context)
    else:
        return redirect('/')
