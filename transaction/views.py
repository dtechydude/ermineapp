from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from business.models import Transact, Comment
from .models import MerchantSetTransact, SubscriberTransact, MerchantCommssion
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import  DetailView, CreateView,  UpdateView, ListView, FormView
from .forms import MerchantSetTransactForm, MerchantTransactionUpdateForm, CommentForm, ReplyForm
from .filters import TransactFilter, MyTransactFilter, Commentilter

# Create your views here.

def set_transaction(request):
    return render(request, 'transaction/merchant_set_transaction.html')

# I am using function base view as above instead of this
class MerchantTransactionCreateView(LoginRequiredMixin, CreateView):
    form_class = MerchantSetTransactForm
    model = MerchantSetTransact
    template_name = 'transaction/merchant_set_transaction.html'

    def get_success_url(self):
        return reverse_lazy('transaction:transaction-detail', kwargs={'pk': self.object.pk})

    
    def form_valid(self, form):
        form.instance.merchant = self.request.user
        return super().form_valid(form)
    
    

class MerchantTransactListView(LoginRequiredMixin, ListView):
    model = MerchantSetTransact
    template_name = 'transaction/my_transaction_list.html'
    context_object_name = 'transaction'
    ordering = ['-trans_date']
   

#Merchant transaction detail view
class MerchantTransactionDetailView(LoginRequiredMixin, DetailView):
    model = MerchantSetTransact
    context_object_name = 'trans_detail'
    template_name = 'transaction/my_transaction_detail.html'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        new_str = self.kwargs.get('pk') or self.request.GET.get('pk') or None

        queryset = queryset.filter(pk=new_str)
        obj = queryset.get()
        return obj

class MerchantTransactUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = MerchantSetTransact
    template_name = 'transaction/transaction_update_form.html'
    fields = ['charges_amount_paid', 'comp_bank_ref', 'max_amount', 'trans_status', 'trans_remark']
    # context_object_name = 'transaction'
    # success_url = reverse_lazy('transaction:transaction-detail', str=id)
    def get_success_url(self):
        return reverse_lazy('transaction:transaction-detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.merchant = self.request.user
        return super().form_valid(form)

    def test_func(self):
        merchantsettransact = self.get_object()
        if self.request.user == merchantsettransact.merchant:
            return True
        return False

class MerchantChargesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = MerchantSetTransact
    template_name = 'transaction/transaction_charges_form.html'
    fields = ['charges_amount_paid', 'comp_bank_ref',]
    # context_object_name = 'transaction'
    # success_url = reverse_lazy('transaction:transaction-detail', str=id)
    def get_success_url(self):
        return reverse_lazy('transaction:transaction-detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.merchant = self.request.user
        return super().form_valid(form)

    def test_func(self):
        merchantsettransact = self.get_object()
        if self.request.user == merchantsettransact.merchant:
            return True
        return False
    

# Subscriber Transact Flow
class SubscriberTransactView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = SubscriberTransact
    template_name = 'transaction/subscriber_reply_form.html'
    fields = ['charges_amount_paid', 'comp_bank_ref',]
    # context_object_name = 'transaction'
    # success_url = reverse_lazy('transaction:transaction-detail', str=id)
    def get_success_url(self):
        return reverse_lazy('transaction:transaction-detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.subscriber = self.request.user
        return super().form_valid(form)

    def test_func(self):
        merchantsettransact = self.get_object()
        if self.request.user == merchantsettransact.merchant:
            return True
        return False


# Transaction Flow view
class TransactionFlowView(DetailView, FormView):
    context_object_name = 'transaction_flow'
    model = MerchantSetTransact
    template_name = 'transaction/transaction_flow.html'
    # for replies to MerchantSetTransact
    form_class = CommentForm
    second_form_class = ReplyForm
    '''
        send two forms to page
        see which one is posted
        take action on the form which is posted
    '''
    def get_context_data(self, **kwargs):
        context = super(TransactionFlowView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class()
        # context['comments] = Comment.objects.filter(id=self.object.id)
        return context


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'form' in request.POST:
            form_class = self.get_form_class()
            form_name = 'form'
        else:
            form_class = self.second_form_class
            form_name = 'form2'

        form = self.get_form(form_class)

        if form_name=='form' and form.is_valid():
            print("comment form is returned")
            return self.form_valid(form)
        elif form_name=='form2' and form.is_valid():
            print("reply form is returned")
            return self.form2_valid(form)

    def get_success_url(self):
        self.object = self.get_object()
        
        return reverse_lazy('transaction:transaction-flow', kwargs={'pk':self.object.pk})
                                                            

    def form_valid(self, form):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.subscriber = self.request.user
        fm.trans_ref = self.object.comments.name
        fm.trans_ref_id = self.object.id
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

    def form2_valid(self, form):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.merchant = self.request.user
        fm.comment_name_id = self.request.POST.get('subscribertransact.id')
        fm.save()
        return HttpResponseRedirect(self.get_success_url())


@login_required
def transaction_history(request):
    transhistory = Transact.objects.all().order_by('-trans_date')
    context = {
        'transhistory':transhistory
    }
    return render(request, 'transaction/transaction_history.html', context)

@login_required
def transaction_status(request):
    return render(request, 'transaction/transaction_status.html')

@login_required
def company_income(request):
    allincome = Transact.objects.all().order_by('-id')
    context = {
        'allincome': allincome
    }
    return render(request, 'transaction/company_income.html', context)

@login_required
def merchant_earning(request):
    merchantearn = Transact.objects.all().order_by('-id')
    context = {
        'merchantearn': merchantearn
    }
    return render(request, 'transaction/merchant_earning.html', context)

# @login_required
def agent_earning(request):
    return render(request, 'transaction/agent_earning.html')

# @login_required
def select_merchant(request):
    selectmerchant = Transact.objects.all().order_by('-id')
    context = {
        'selectmerchant': selectmerchant
    }
    return render(request, 'transaction/select_merchant.html', context)



# Merchant
@login_required
def view_self_transaction(request):
    mytransact = Transact.objects.filter(created_by=User.objects.get(username=request.user))
    mytransact_filter = MyTransactFilter(request.GET, queryset=mytransact)
    mytransact = mytransact_filter.qs

    context = {
        # 'mypayment' : PaymentDetail.objects.filter(student=StudentDetail.objects.get(user=request.user)).order_by("-payment_date"),
        'mytransact' : Transact.objects.filter(created_by=User.objects.get(username=request.user)).order_by("created_at"),
        'mytransact':mytransact,
        'mytransact_filter' : mytransact_filter,
    }

    return render(request, 'transaction/view_self_transaction.html', context)


# Subscriber
@login_required
def subscriber_self_transaction(request):
    mytransact = Comment.objects.filter(author=User.objects.get(username=request.user))
    
    context = {
        'mytransact' : Comment.objects.filter(author=User.objects.get(username=request.user)).order_by("date_added"),
        'mytransact':mytransact,
    }

    return render(request, 'transaction/subscriber_self_transaction.html', context)