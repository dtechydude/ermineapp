from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

# @login_required
def transaction_history(request):
    return render(request, 'transaction/transaction_history.html')

# @login_required
def transaction_status(request):
    return render(request, 'transaction/transaction_status.html')

# @login_required
def company_income(request):
    return render(request, 'transaction/company_income.html')

# @login_required
def merchant_earning(request):
    return render(request, 'transaction/merchant_earning.html')

# @login_required
def agent_earning(request):
    return render(request, 'transaction/agent_earning.html')