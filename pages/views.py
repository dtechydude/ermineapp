from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import Profile
from django.contrib.auth.models import User


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

# @login_required
def company_charges_chart(request):
    allcharges = User.objects.all().order_by('-id')
    context = {
        'allcharges': allcharges

    }
    # return render(request, 'merchant/merchant_list.html', context)
    return render(request, 'pages/company_charges_chart.html', context)

def subscriber_charges_chart(request):
    return render(request, 'pages/subscriber_charges_chart.html')

def company_bank_detail(request):
    return render(request, 'pages/company_bank_detail.html')

def privacy_policy(request):
    return render(request, 'pages/privacy_policy.html')