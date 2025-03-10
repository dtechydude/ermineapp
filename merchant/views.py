from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Profile
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from transaction.models import MerchantSetTransact
from .models import Merchant
from .forms import MerchantUpdateForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView


#Displays available merchants to subscribers
def available_merchant(request):
    available = MerchantSetTransact.objects.all()
    context ={
        'available':available
    }
    return render(request, 'merchant/available_merchant.html', context)

def merchant_detail(request):
    return render(request, 'merchant/merchant_detail.html')

#Displays all merchants
def merchant_list(request):
    allmerchant = Merchant.objects.all().order_by('-id')
    context = {
        'allmerchant': allmerchant

    }
    return render(request, 'merchant/merchant_list.html', context)


class MerchantDetailView(DetailView):
    template_name = 'merchant/merchant_detail.html'
    queryset = Merchant.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Merchant, id=id_)


class MerchantUpdateView(LoginRequiredMixin, UpdateView):
    form_class = MerchantUpdateForm
    template_name = 'merchant/merchant_update_form.html'
    # queryset = StudentDetail.objects.all()


    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Merchant, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class MerchantDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'merchant/merchant_delete.html'
    success_url = reverse_lazy('merchant:merchant-list')
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Merchant, id=id_)


