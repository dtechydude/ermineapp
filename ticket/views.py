from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import(TemplateView, DetailView,
                                ListView, FormView, CreateView, 
                                UpdateView, DeleteView)
from .models import Ticket, save_lesson_files, Group, Subject
from .forms import CommentForm, TicketForm, ReplyForm, 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from students.models import StudentDetail


class GroupSelfListView(LoginRequiredMixin, ListView):
    context_object_name = 'groups'
    model = Group
    template_name = 'ticket/my_class.html'
 
    # Student can only view their class elearning
    def get_queryset(self):
        return Group.objects.filter(name = self.request.user.profile)

# Standard list view for the admin and teachers
class GroupListView(LoginRequiredMixin, ListView):
    context_object_name = 'groups'
    model = Group
    # template_name = 'curriculum/class_list.html'
    template_name = 'ticket/elearning_class.html'

    
class SubjectListView(DetailView):
    context_object_name = 'groups'
    model = Group
    template_name = 'ticket/class_subjects.html'


class TicketListView(DetailView):
    context_object_name = 'subjects'
    model = Subject
    template_name = 'ticket/course_list.html'


class TicketDetailView(DetailView, FormView):
    context_object_name = 'tickets'
    model = Ticket
    template_name = 'ticket/lesson-detail.html'
    # for replies to lessons
    form_class = CommentForm
    second_form_class = ReplyForm
    '''
        send two forms to page
        see which one is posted
        take action on the form which is posted
    '''
    def get_context_data(self, **kwargs):
        context = super(TicketDetailView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class()
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
        group = self.object.group
        subject = self.object.subject
        return reverse_lazy('ticket:ticket_detail', kwargs={'group':group.slug,
                                                            'subject':subject.slug,
                                                            'slug':self.object.slug})

    def form_valid(self, form):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.author = self.request.user
        fm.ticket_name = self.object.comments.name
        fm.ticket_name_id = self.object.id
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

    def form2_valid(self, form):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.author = self.request.user
        fm.comment_name_id = self.request.POST.get('comment.id')
        fm.save()
        return HttpResponseRedirect(self.get_success_url())
            

class TicketCreateView(CreateView):
    form_class = TicketForm
    context_object_name = 'subject'
    model = Subject
    template_name = 'ticket/lesson_create.html'

    def get_success_url(self):
        self.object = self.get_object()
        standard = self.object.standard
        return reverse_lazy('ticket:lesson_list',kwargs={'group':standard.slug, 'slug':self.object.slug})

    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.created_by = self.request.user
        fm.group = self.object.group
        fm.subject = self.object
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

class TicketUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    fields = ('name', 'comment')
    model = Ticket
    template_name = 'ticket/lesson_update_view.html'
    context_object_name = 'tickets'
    
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


class TicketDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ticket
    context_object_name = 'tickets'
    template_name = 'ticket/lesson_delete.html'

    def get_success_url(self):
        group = self.object.group
        subject = self.object.subject
        return reverse_lazy('ticket:ticket_list', kwargs={'group':group.slug, 'slug':subject.slug})

#preventing other users from update other people's post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.created_by:
            return True
        return False
