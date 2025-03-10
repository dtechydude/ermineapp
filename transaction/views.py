from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import MerchantSetTransact, SubscriberTransact

# Create your views here.

# @login_required
def transaction_history(request):
    transhistory = SubscriberTransact.objects.all().order_by('-trans_date')
    context = {
        'transhistory':transhistory
    }
    return render(request, 'transaction/transaction_history.html', context)

# @login_required
def transaction_status(request):
    return render(request, 'transaction/transaction_status.html')

# @login_required
def company_income(request):
    allincome = MerchantSetTransact.objects.all().order_by('-id')
    context = {
        'allincome': allincome
    }
    return render(request, 'transaction/company_income.html', context)

# @login_required
def merchant_earning(request):
    merchantearn = SubscriberTransact.objects.all().order_by('-id')
    context = {
        'merchantearn': merchantearn
    }
    return render(request, 'transaction/merchant_earning.html', context)

# @login_required
def agent_earning(request):
    return render(request, 'transaction/agent_earning.html')

# @login_required
def select_merchant(request):
    selectmerchant = MerchantSetTransact.objects.all().order_by('-id')
    context = {
        'selectmerchant': selectmerchant
    }
    return render(request, 'transaction/select_merchant.html', context)