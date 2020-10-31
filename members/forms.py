from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from book.models import Profile


class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'website_url')

        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'website_url': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProfilePageForm, self).__init__(*args, **kwargs)
        self.fields['profile_pic'].label = "Profile Picture"
        self.fields['website_url'].label = "Website URL"


class EditProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'website_url')

        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'website_url': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(EditProfilePageForm, self).__init__(*args, **kwargs)
        self.fields['profile_pic'].label = "Profile Picture"
        self.fields['website_url'].label = "Website URL - No need to prefix with www or https"


class EditSettingsForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_staff = forms.CharField(
        max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_active = forms.CharField(
        max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    last_login = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'style': 'background:none; border:none'}))
    date_joined = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'style': 'background:none; border:none'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',
                  'is_staff', 'is_active', 'last_login', 'date_joined', 'password')

    def __init__(self, *args, **kwargs):
        super(EditSettingsForm, self).__init__(*args, **kwargs)
        self.fields['last_login'].widget.attrs['readonly'] = True
        self.fields['date_joined'].widget.attrs['readonly'] = True


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password', 'label': 'New Password Change'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = Profile
        fields = ('old_password', 'new_password1', 'new_password2')

    def __init__(self, *args, **kwargs):
        super(PasswordChangingForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].label = "Current Password"
        self.fields['new_password1'].label = "New Password"
        self.fields['new_password2'].label = "Verify Password"
