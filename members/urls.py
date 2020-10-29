
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from members import views
from . import views
from .views import UserEditView, CreateProfilePageView, ShowProfilePageView, EditProfilePageView, PasswordsChangeView

urlpatterns = [
    # User auth
    path('signupuser/', views.signupuser, name='signupuser'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    
    # User settings
    path('edit_settings/', UserEditView.as_view(), name='edit_settings'),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_password.html')),
    path('password_success/', views.password_success, name="password_success"),
        
     # User profile
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
]
