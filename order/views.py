from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import(TemplateView, DetailView,
                                ListView, FormView, CreateView, 
                                UpdateView, DeleteView)
from .models import Order, State, Lga
from .forms import CommentForm, OrderForm, ReplyForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from users.models import Profile


class StateSelfListView(LoginRequiredMixin, ListView):
    context_object_name = 'state'
    model = State
    # template_name = 'curriculum/class_list.html'
    template_name = 'order/my_class.html'
 
    # Student can only view their class elearning
    def get_queryset(self):
        return State.objects.filter(name = self.request.user.profile.current_state)
        # return State.objects.filter(name = self.request.user)

# Standard list view for the admin and teachers
class StateListView(LoginRequiredMixin, ListView):
    context_object_name = 'states'
    model = State
    # template_name = 'curriculum/class_list.html'
    template_name = 'order/elearning_class.html'

    
class LgaListView(DetailView):
    context_object_name = 'states'
    model = State
    template_name = 'order/class_subjects.html'


class OrderListView(DetailView):
    context_object_name = 'lgas'
    model = Lga
    template_name = 'order/course_list.html'


class OrderDetailView(DetailView, FormView):
    context_object_name = 'lessons'
    model = Order
    template_name = 'order/lesson-detail.html'
    # for replies to lessons
    form_class = CommentForm
    second_form_class = ReplyForm
    '''
        send two forms to page
        see which one is posted
        take action on the form which is posted
    '''
    def get_context_data(self, **kwargs):
        context = super(OrderDetailView, self).get_context_data(**kwargs)
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
        lga = self.object.lga
        return reverse_lazy('order:order_detail', kwargs={'state':state.slug,
                                                            'lga':lga.slug,
                                                            'slug':self.object.slug})

    def form_valid(self, form):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.author = self.request.user
        fm.order_name = self.object.comments.name
        fm.order_name_id = self.object.id
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

    def form2_valid(self, form):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.author = self.request.user
        fm. comment_name_id = self.request.POST.get('comment.id')
        fm.save()
        return HttpResponseRedirect(self.get_success_url())
            



class OrderCreateView(CreateView):
    form_class = OrderForm
    context_object_name = 'subject'
    model = Lga
    template_name = 'order/lesson_create.html'

    def get_success_url(self):
        self.object = self.get_object()
        state = self.object.state
        return reverse_lazy('order:lesson_list',kwargs={'state':state.slug, 'slug':self.object.slug})

    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.created_by = self.request.user
        fm.state = self.object.state
        fm.lga = self.object
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

class OrderUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    fields = ('name', 'position', 'video', 'comment')
    model = Order
    template_name = 'curriculum/lesson_update_view.html'
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


class OrderDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Order
    context_object_name = 'orders'
    template_name = 'order/lesson_delete.html'

    def get_success_url(self):
        state = self.object.state
        lga = self.object.lga
        return reverse_lazy('order:lesson_list', kwargs={'state':state.slug, 'slug':lga.slug})

#preventing other users from update other people's post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.created_by:
            return True
        return False



   