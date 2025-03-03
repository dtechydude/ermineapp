from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def transaction_history(request):
    return render(request, 'transaction/transaction_history.html')