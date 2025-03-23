from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import(TemplateView, DetailView,
                                ListView, FormView, CreateView, 
                                UpdateView, DeleteView)
from .models import Lesson, Standard, Subject, save_lesson_files
from .forms import CommentForm, LessonForm, ReplyForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from users.models import Profile


class StandardSelfListView(LoginRequiredMixin, ListView):
    context_object_name = 'standards'
    model = Standard
    template_name = 'business/my_class.html'
 
    # Student can only view their class elearning
    def get_queryset(self):
        return Standard.objects.filter(name = self.request.user.profile.current_state)

# Standard list view for the admin and teachers
class StandardListView(LoginRequiredMixin, ListView):
    context_object_name = 'standards'
    model = Standard
    template_name = 'business/state_list.html'

    
class SubjectListView(DetailView):
    context_object_name = 'standards'
    model = Standard
    template_name = 'business/class_subjects.html'


class LessonListView(DetailView):
    context_object_name = 'subjects'
    model = Subject
    template_name = 'business/course_list.html'


class LessonDetailView(DetailView, FormView):
    context_object_name = 'lessons'
    model = Lesson
    template_name = 'business/lesson-detail.html'
    # for replies to lessons
    form_class = CommentForm
    second_form_class = ReplyForm
    '''
        send two forms to page
        see which one is posted
        take action on the form which is posted
    '''
    def get_context_data(self, **kwargs):
        context = super(LessonDetailView, self).get_context_data(**kwargs)
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
        standard = self.object.standard
        subject = self.object.subject
        return reverse_lazy('business:lesson_detail', kwargs={'standard':standard.slug,
                                                            'subject':subject.slug,
                                                            'slug':self.object.slug})

    def form_valid(self, form):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.author = self.request.user
        fm.lesson_name = self.object.comments.name
        fm.lesson_name_id = self.object.id
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

    def form2_valid(self, form):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.author = self.request.user
        fm. comment_name_id = self.request.POST.get('comment.id')
        fm.save()
        return HttpResponseRedirect(self.get_success_url())
            



class LessonCreateView(CreateView):
    form_class = LessonForm
    context_object_name = 'subject'
    model = Subject
    template_name = 'business/lesson_create.html'

    def get_success_url(self):
        self.object = self.get_object()
        standard = self.object.standard
        return reverse_lazy('business:lesson_list',kwargs={'standard':standard.slug, 'slug':self.object.slug})

    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.created_by = self.request.user
        fm.standard = self.object.standard
        fm.subject = self.object
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

class LessonUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    fields = ('name', 'position', 'video', 'comment')
    model = Lesson
    template_name = 'business/lesson_update_view.html'
    context_object_name = 'lessons'
    
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


class LessonDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Lesson
    context_object_name = 'lessons'
    template_name = 'business/lesson_delete.html'

    def get_success_url(self):
        standard = self.object.standard
        subject = self.object.subject
        return reverse_lazy('business:lesson_list', kwargs={'standard':standard.slug, 'slug':subject.slug})

#preventing other users from update other people's post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.created_by:
            return True
        return False



   