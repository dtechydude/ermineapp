from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from users.models import Profile
from django.contrib.auth.models import User
from django.views.generic import(TemplateView, DetailView,
                                ListView, FormView, CreateView, 
                                UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import(ProfileUpdateForm, UserUpdateForm, KYCUpdateForm,
                   BusinessUpdateForm, UserTwoUpdateForm, BankUpdateForm,
                   RoleUpdateForm, BioUpdateForm, AddressUpdateForm, PhoneUpdateForm)




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

    return render(request, 'users/profile_update_form.html', context)


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
        id_ = self.kwargs.get('id')
        return get_object_or_404(Profile, id=id_)
  

class UserDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'users/users_delete.html'
    success_url = reverse_lazy('users:members-list')
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Profile, id=id_)
    # queryset = StudentDetail.objects.all()

# Profile Information
@login_required
def profileupdate(request):
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


# Business Information
@login_required
def business_profile(request):
    if request.method == 'POST':
        u_form = UserTwoUpdateForm(request.POST, instance=request.user)
        p_form = BusinessUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your business information has been updated successfully')
            return redirect('pages:dashboard')
    else:
        u_form = UserTwoUpdateForm(instance=request.user)
        p_form = BusinessUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/business_update_form.html', context)

# Bank Profile Information
@login_required
def bankprofile(request):
    if request.method == 'POST':
        u_form = UserTwoUpdateForm(request.POST, instance=request.user)
        p_form = BankUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Bank Profile has been updated successfully')
            return redirect('pages:dashboard')
    else:
        u_form = UserTwoUpdateForm(instance=request.user)
        p_form = BankUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/bank_update_form.html', context)

# KYC information
@login_required
def kycprofile(request):
    if request.method == 'POST':
        u_form = UserTwoUpdateForm(request.POST, instance=request.user)
        p_form = KYCUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your KYC information has been updated successfully')
            return redirect('pages:dashboard')
    else:
        u_form = UserTwoUpdateForm(instance=request.user)
        p_form = KYCUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/kyc_update_form.html', context)

# KYC information
@login_required
def roleprofile(request):
    if request.method == 'POST':
        u_form = UserTwoUpdateForm(request.POST, instance=request.user)
        p_form = RoleUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your ROLE switch has been updated successfully')
            return redirect('pages:dashboard')
    else:
        u_form = UserTwoUpdateForm(instance=request.user)
        p_form = RoleUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/user_role_update.html', context)

@login_required
def bioprofile(request):
    if request.method == 'POST':
        u_form = UserTwoUpdateForm(request.POST, instance=request.user)
        p_form = BioUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your ROLE switch has been updated successfully')
            return redirect('pages:dashboard')
    else:
        u_form = UserTwoUpdateForm(instance=request.user)
        p_form = BioUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/bio_update.html', context)

# Address Update
@login_required
def phoneprofile(request):
    if request.method == 'POST':
        u_form = UserTwoUpdateForm(request.POST, instance=request.user)
        p_form = PhoneUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your ROLE switch has been updated successfully')
            return redirect('pages:dashboard')
    else:
        u_form = UserTwoUpdateForm(instance=request.user)
        p_form = PhoneUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/phone_update.html', context)

# Address Update
@login_required
def addressprofile(request):
    if request.method == 'POST':
        u_form = UserTwoUpdateForm(request.POST, instance=request.user)
        p_form = AddressUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your ROLE switch has been updated successfully')
            return redirect('pages:dashboard')
    else:
        u_form = UserTwoUpdateForm(instance=request.user)
        p_form = AddressUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/address_update.html', context)