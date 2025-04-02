from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Profile
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import AgentList
from .forms import AgentRegisterForm
from django.views.generic import CreateView




#Displays all merchants
@login_required
def agent_list(request):
    allagent = Profile.objects.filter(user_role='agent').order_by('-id')
    context = {
        'allagent': allagent

    }
    return render(request, 'agent/agent_list.html', context)

@login_required
def free_agent(request):
    free = AgentList.objects.all().order_by('-id')
    context = {
        'free': free

    }
    return render(request, 'agent/agent_list.html', context)



class AgentCreateView(CreateView): 
    fields = ['username', 'phone', 'email', 'first_name', 'last_name']
    model = AgentList
    template_name = 'agent/agent_create.html'
    success_message = "Your Transaction was updated successfully"

    def get_success_url(self):
        return reverse('agent:agent-reg-confirm')
    

def agent_reg_confirm(request):
    return render(request, 'agent/agent_reg_confirm.html')
    