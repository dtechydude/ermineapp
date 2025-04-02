from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Profile
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from transaction.models import MerchantSetTransact
from .models import Merchant, Cooperative
from business.models import Transact
from .forms import MerchantUpdateForm, MerchantRegisterForm, MerchantForm, CooperativeForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, FormView, CreateView


#Displays available merchants to subscribers
def available_merchant(request):
    available = Transact.objects.filter(payment_confirmed=True).order_by('-trans_date')

    context ={
        'available':available
    }
    return render(request, 'merchant/available_merchant.html', context)

def merchant_detail(request):
    return render(request, 'merchant/merchant_detail.html')

#Displays all merchants
def merchant_list(request):
    allmerchant = Profile.objects.filter(user_role='merchant').order_by('-id')
    context = {
        'allmerchant': allmerchant

    }
    return render(request, 'merchant/merchant_list.html', context)

def my_earning(request):
    myearning = Transact.objects.filter(created_by=request.user).order_by('-id')
    context = {
        'myearning': myearning

    }
    return render(request, 'merchant/my_earning.html', context)


#merchant create function
@login_required
def merchantform(request):
    if request.method == 'POST':
        merchant_form = MerchantForm(request.POST, instance=request.user)
        if merchant_form.is_valid():
            merchant_form.save()
            messages.success(request, f'Your profile has been updated successfully')
            return redirect('pages:dashboard')
    else:
        merchant_form = MerchantForm(instance=request.user)

    context = {
        'merchant_form': merchant_form,
        
    }

    return render(request, 'merchant/merchant_create.html', context)


#merchant create Class Base View
class MerchantCreateView(CreateView):
    form_class = MerchantForm
    context_object_name = 'merchant'
    model = Merchant
    template_name = 'merchant/merchant_create.html'

    def get_success_url(self):
        self.object = self.get_object()
        # profile = self.object.profile
        return reverse_lazy('merchant:merchant_list',kwargs={'slug':self.object.slug})

    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.profile = self.request.user
        fm.save()
        return HttpResponseRedirect(self.get_success_url())



class MerchantDetailView(LoginRequiredMixin, DetailView):
    template_name = 'merchant/merchant_detail.html'
    queryset = Merchant.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Merchant, id=id_)


class MerchantUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = MerchantUpdateForm
    # template_object_name = 'merchant'
    template_name = 'merchant/merchant_update_form.html'
    # queryset = StudentDetail.objects.all()


    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Merchant, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
    #preventing other users from update other people's post
    def test_func(self):
        merchant = self.get_object()
        if self.request.user == merchant.profile.user:
            return True
        return False

class MerchantDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'merchant/merchant_delete.html'
    success_url = reverse_lazy('merchant:merchant-list')
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Merchant, id=id_)



# Transaction Flow view
class TransactionFlowView(DetailView, FormView):
    pass
    


class CooperativeCreateView(CreateView):
    form_class = CooperativeForm
    context_object_name = 'subject'
    model = Cooperative
    template_name = 'business/create.html'
    success_message = "Your Transaction was updated successfully"

    def get_success_url(self):
        self.object = self.get_object()
        state = self.object.state
        return reverse_lazy('business:transact_list',kwargs={'state':state.slug, 'slug':self.object.slug})

    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.created_by = self.request.user
        fm.state = self.object.state
        fm.subject = self.object
        fm.save()
        return HttpResponseRedirect(self.get_success_url())


