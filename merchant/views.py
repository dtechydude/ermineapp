from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Profile


#Displays available merchants to subscribers
def available_merchant(request):
    return render(request, 'merchant/available_merchant.html')

def merchant_detail(request):
    return render(request, 'merchant/merchant_detail.html')

#Displays all merchants
def merchant_list(request):
    allmerchant = User.objects.all().order_by('-id')
    context = {
        'allmerchant': allmerchant

    }
    return render(request, 'merchant/merchant_list.html', context)



