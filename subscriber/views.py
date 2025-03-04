from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# @login_required
def subscriber_detail(request):
    return render(request, 'subscriber/subscriber_detail.html')
