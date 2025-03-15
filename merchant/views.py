from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Profile
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from transaction.models import MerchantSetTransact
from .models import Merchant
from .forms import MerchantUpdateForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, FormView


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



# Transaction Flow view
class TransactionFlowView(DetailView, FormView):
    pass
    # context_object_name = 'transaction_flow'
    # model = MerchantSetTransactForm
    # template_name = 'transaction/transaction_flow.html'
    # # for replies to MerchantSetTransact
    # form_class = CommentForm
    # second_form_class = ReplyForm
    # '''
    #     send two forms to page
    #     see which one is posted
    #     take action on the form which is posted
    # '''
    # def get_context_data(self, **kwargs):
    #     context = super(TransactionFlowView, self).get_context_data(**kwargs)
    #     if 'form' not in context:
    #         context['form'] = self.form_class()
    #     if 'form2' not in context:
    #         context['form2'] = self.second_form_class()
    #     # context['comments] = Comment.objects.filter(id=self.object.id)
    #     return context


    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     if 'form' in request.POST:
    #         form_class = self.get_form_class()
    #         form_name = 'form'
    #     else:
    #         form_class = self.second_form_class
    #         form_name = 'form2'

    #     form = self.get_form(form_class)

    #     if form_name=='form' and form.is_valid():
    #         print("comment form is returned")
    #         return self.form_valid(form)
    #     elif form_name=='form2' and form.is_valid():
    #         print("reply form is returned")
    #         return self.form2_valid(form)

    # def get_success_url(self):
    #     self.object = self.get_object()
    #     standard = self.object.standard
    #     subject = self.object.subject
    #     return reverse_lazy('transaction:transaction-flow', kwargs={'id':self.object.id})
                                                            

    # def form_valid(self, form):
    #     self.object = self.get_object()
    #     fm = form.save(commit=False)
    #     fm.subscriber = self.request.user
    #     fm.trans_ref = self.object.comments.name
    #     fm.trans_ref_id = self.object.id
    #     fm.save()
    #     return HttpResponseRedirect(self.get_success_url())

    # def form2_valid(self, form):
    #     self.object = self.get_object()
    #     fm = form.save(commit=False)
    #     fm.merchant = self.request.user
    #     fm.comment_name_id = self.request.POST.get('subscribertransact.id')
    #     fm.save()
    #     return HttpResponseRedirect(self.get_success_url())
