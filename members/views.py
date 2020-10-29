from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.models import User
from book.models import Profile
from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, AuthenticationForm
from .forms import ProfilePageForm, EditSettingsForm, EditProfilePageForm, PasswordChangingForm
from django.contrib.auth.views import PasswordChangeView
from django.views import generic
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages


# Auth functions
def signupuser(request):
    if request.method == 'GET':
        return render(request, 'registration/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currentbooks')
            except IntegrityError:
                messages.error(request, 'User already exists.')
                return render(request, 'registration/signupuser.html', {'form': UserCreationForm()})
        else:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'registration/signupuser.html', {'form': UserCreationForm()})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'registration/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            messages.error(
                request, 'Username does not exist, or you entered the wrong password.')
            return render(request, 'registration/loginuser.html', {'form': AuthenticationForm()})

        else:
            login(request, user)
            messages.success(request, 'Logged in successfully.')
            return redirect('currentbooks')


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'Logged out successfully!')
        return redirect('loginuser')


# Profile classes
class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile_page.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfilePageView(UpdateView):
    model = Profile
    form_class = EditProfilePageForm
    template_name = 'registration/edit_profile_page.html'
    success_url = reverse_lazy('home')


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView,
                        self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        print(page_user)
        context["page_user"] = page_user
        print(f'Context: {context}')
        return context

# User settings


class UserEditView(generic.UpdateView):
    form_class = EditSettingsForm
    template_name = 'registration/edit_settings.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')


def password_success(request):
    messages.success(request, 'Password changed successfully.')
    return render(request, 'registration/password_success.html', {})
