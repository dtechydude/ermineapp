from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import Profile
from django.contrib.auth.models import User
from merchant.models import Merchant
from subscriber.models import SubscriberList
from users.models import Profile
from transaction.models import MerchantSetTransact, SubscriberTransact
from agent.models import AgentList


def ermine_home(request):
    return render(request, 'pages/apphome.html')


@login_required
def dashboard(request):
    users_num = User.objects.count()
    merchant_num = Merchant.objects.count()
    subscriber_num = SubscriberList.objects.count()
    agent_num = AgentList.objects.count()
    inactive_user = User.objects.filter(is_active=False).count()
    total_trans = MerchantSetTransact.objects.count()
    suspended_user = Profile.objects.filter(user_status='suspended').count()
    my_trans = MerchantSetTransact.objects.filter(merchant=User.objects.get(username=request.user)).count()
    sub_trans = SubscriberTransact.objects.filter(subscriber=User.objects.get(username=request.user)).count()

    context = {
        'merchant_num': merchant_num,
        'inactive_user' : inactive_user,
        'users_num': users_num,
        'subscriber_num': subscriber_num,
        'suspended_user': suspended_user,
        'total_trans': total_trans,
        'my_trans': my_trans,
        'sub_trans': sub_trans,
        'agent_num': agent_num,
    }
    return render(request, 'pages/dashboard.html', context)

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

# @login_required
def subscriber_charges_chart(request):
    return render(request, 'pages/subscriber_charges_chart.html')

# @login_required
def company_bank_detail(request):
    return render(request, 'pages/company_bank_detail.html')

# @login_required
def privacy_policy(request):
    return render(request, 'pages/privacy_policy.html')

# @login_required
def referral_link(request):
    return render(request, 'pages/referral_link.html')


def error_page (request):
    return render(request, 'pages/error_page.html')

def cooperative_page(request):
    return render(request, 'pages/cooperative.html')

