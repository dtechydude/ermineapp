from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import SubscriberList
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from django.urls import reverse, reverse_lazy
from .forms import SubscriberRegisterForm, SubscriberUpdateForm




# @login_required
def subscriber_list(request):
    subscriber = SubscriberList.objects.all().order_by('-id')
    context = {
        'subscriber' : subscriber,       

    }

    return render(request, 'subscriber/subscriber_list.html', context)

# @login_required
def subscriber_detail(request):
    return render(request, 'subscriber/subscriber_detail.html')


class SubscriberDetailView(DetailView):
    template_name = 'subscriber/subscriber_detail.html'
    queryset = SubscriberList.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(SubscriberList, id=id_)


class SubscriberUpdateView(LoginRequiredMixin, UpdateView):
    form_class = SubscriberUpdateForm
    template_name = 'subscriber/subscriber_update_form.html'
    # queryset = StudentDetail.objects.all()


    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(SubscriberList, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class SubscriberDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'subscriber/subscriber_delete.html'
    success_url = reverse_lazy('subscriber:subscriber-list')
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(SubscriberList, id=id_)
    

# class StudentDeleteView(LoginRequiredMixin, DeleteView):
#     template_name = 'subscriber/subscriber_delete.html'
#     success_url = reverse_lazy('subscriber:subscriber-list')
    
#     def get_object(self):
#         id_ = self.kwargs.get("id")
#         return get_object_or_404(SubscriberList, id=id_)
#     # queryset = StudentDetail.objects.all()

