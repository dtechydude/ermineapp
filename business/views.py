from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import(TemplateView, DetailView,
                                ListView, FormView, CreateView, 
                                UpdateView, DeleteView)
from .models import Transact, State, Subject, save_transact_files
from .forms import CommentForm, TransactForm, ReplyForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from users.models import Profile


class StateSelfListView(LoginRequiredMixin, ListView):
    context_object_name = 'states'
    model = State
    template_name = 'business/my_state.html'
 
    # Student can only view their class elearning
    def get_queryset(self):
        return State.objects.filter(name = self.request.user.profile.current_state)

# Standard list view for the admin and teachers
class StateListView(LoginRequiredMixin, ListView):
    context_object_name = 'states'
    model = State
    template_name = 'business/state_list.html'

    
class SubjectListView(DetailView):
    context_object_name = 'states'
    model = State
    template_name = 'business/class_subjects.html'


class TransactListView(DetailView):
    context_object_name = 'subjects'
    model = Subject
    template_name = 'business/transact_list.html'
    # queryset = Subject.objects.all()

    # def get_object(self):
    #     slug_ = self.kwargs.get("slug")
    #     return get_object_or_404(Subject, slug=slug_)


class TransactDetailView(DetailView, FormView):
    context_object_name = 'transacts'
    model = Transact
    template_name = 'business/transact-detail.html'
    # for replies to lessons
    form_class = CommentForm
    second_form_class = ReplyForm
    '''
        send two forms to page
        see which one is posted
        take action on the form which is posted
    '''
    def get_context_data(self, **kwargs):
        context = super(TransactDetailView, self).get_context_data(**kwargs)
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
        state = self.object.state
        subject = self.object.subject
        return reverse_lazy('business:transact_detail', kwargs={'state':state.slug,
                                                            'subject':subject.slug,
                                                            'slug':self.object.slug})

    def form_valid(self, form):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.author = self.request.user
        fm.transact_name = self.object.comments.name
        fm.transact_name_id = self.object.id
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

    def form2_valid(self, form):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.author = self.request.user
        fm. comment_name_id = self.request.POST.get('comment.id')
        fm.save()
        return HttpResponseRedirect(self.get_success_url())
            



class TransactCreateView(CreateView):
    form_class = TransactForm
    context_object_name = 'subject'
    model = Subject
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

class TransactUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    fields = ('max_amount', 'min_amount', 'prefered_method', 'state', 'remark')
    model = Transact
    template_name = 'business/transact_update_view.html'
    context_object_name = 'transacts'
    
    #function to check if user is the login user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    #preventing other users from update other people's post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.created_by:
            return True
        return False
    
class ChargesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    fields = ('charges_pay_date', 'charges_amount_paid', 'comp_bank_ref')
    model = Transact
    template_name = 'business/charges_update_form.html'
    context_object_name = 'transacts'
    
    #function to check if user is the login user
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    #preventing other users from update other people's post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.created_by:
            return True
        return False


#Complete Transaction
class TransactCompleteView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    fields = ('end_trans',)
    model = Transact
    template_name = 'business/transact_complete_view.html'
    context_object_name = 'transacts'
    
    #function to check if user is the login user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    #preventing other users from update other people's post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.created_by:
            return True
        return False


class TransactDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Transact
    context_object_name = 'transacts'
    template_name = 'business/transact_delete.html'

    def get_success_url(self):
        state = self.object.state
        subject = self.object.subject
        return reverse_lazy('business:transact_list', kwargs={'state':state.slug, 'slug':subject.slug})

#preventing other users from update other people's post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.created_by:
            return True
        return False



   