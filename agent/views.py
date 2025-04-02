from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Profile
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin




#Displays all merchants
@login_required
def agent_list(request):
    allagent = Profile.objects.filter(user_role='agent').order_by('-id')
    context = {
        'allagent': allagent

    }
    return render(request, 'agent/agent_list.html', context)

