from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def available_merchant(request):
    return render(request, 'merchant/available_merchant.html')

def merchant_detail(request):
    return render(request, 'merchant/merchant_detail.html')


