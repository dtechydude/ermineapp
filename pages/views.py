from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def ermine_home(request):
    return render(request, 'pages/apphome.html')


@login_required
def dashboard(request):
    return render(request, 'pages/dashboard.html')

def lockscreen(request):
    return render(request, 'pages/lockscreen.html')

def logout(request):
    return render(request, 'pages/logout.html')

# @login_required
def help_center(request):
    return render(request, 'pages/help_center.html')