from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from .models import Profile
from django.views.generic import(TemplateView, DetailView,
                                ListView, FormView, CreateView, 
                                UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import ProfileUpdateForm, UserUpdateForm


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated successfully')
            return redirect('users:profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile.html', context)


def my_recommendations_view(request):
    profile = Profile.objects.get(user=request.user)
    my_recs = profile.get_recommended_profiles()

    context = {'my_recs': my_recs}
    return render(request, 'users/main.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'New user account has been created!' )
            return redirect('pages:lock-screen')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('pages:logout'))

# class LogoutView(View):
#     def get(self, request):
#         logout(request)
#         return redirect('users:login')

@login_required
def members_list(request):
    allusers = Profile.objects.all().order_by('-id')
    subscriber = Profile.objects.filter(user_role='subscriber').order_by('-id')
    context = {
        'allusers':allusers,
        'subscriber':subscriber,
    }
    return render(request, 'users/members_list.html', context)

# Members KYC list
def members_kyc_list(request):
    allmembers = Profile.objects.all().order_by('-id')
    context = {
        'allmembers':allmembers,
        
    }
    return render(request, 'users/members_kyc_list.html', context)


class UsersListView(LoginRequiredMixin, ListView):
    context_object_name = 'members'
    model = Profile
    # template_name = 'curriculum/class_list.html'
    template_name = 'users/members_list.html'


class UserDetailView(DetailView):
    template_name = 'users/profile_detail.html'
    queryset = Profile.objects.all()
    # context_object_name = 'profile'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Profile, id=id_)
    
# class UserUpdateView(LoginRequiredMixin, UpdateView):
#     form_class = ProfileUpdateForm
#     template_name = 'users/users_update_form.html'
#     # queryset = Profile.objects.all()


    # def get_object(self):
    #     id_ = self.kwargs.get("id")
    #     return get_object_or_404(StudentDetail, id=id_)

    # def form_valid(self, form):
    #     print(form.cleaned_data)
    #     return super().form_valid(form)

class UserDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'users/users_delete.html'
    success_url = reverse_lazy('users:members-list')
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Profile, id=id_)
    # queryset = StudentDetail.objects.all()


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated successfully')
            return redirect('pages:dashboard')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile_update_form.html', context)