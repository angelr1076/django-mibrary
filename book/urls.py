
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from book import views

urlpatterns = [
    # Default path
    path('', views.home, name='home'),
    
    # Book paths
    path('create/', views.createbook, name='createbook'),
    path('current/', views.currentbooks, name='currentbooks'),
    path('wanttoread/', views.wanttoreadbooks, name='wanttoreadbooks'),
    path('currentlyreading/', views.currentlyreading, name='currentlyreading'),
    path('read/', views.read, name='read'),
    
    path('book/<int:book_pk>', views.viewbook, name='viewbook'),
    path('book/<int:book_pk>/editbook', views.editbook, name='editbook'),
    path('book/<int:book_pk>/viewonly', views.viewonly, name='viewonly'),
    path('book/<int:book_pk>/delete', views.deletebook, name='deletebook'),
    
    # Genres
    path('genre/', AddGenreView.as_view(), name='addgenre'),
]



