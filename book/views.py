from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.db import IntegrityError
from .forms import BookForm, ViewOnlyForm, ReviewForm
from .models import Book, Review, Genre
from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import requests
from django.contrib import messages


# Home
def home(request):
    book_list = Book.objects.all()
    paginator = Paginator(book_list, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'book/home.html', {'page_obj': page_obj, 'book_list': book_list})


# Create    
@login_required
def createbook(request):
    if request.method == 'GET':
        form = BookForm()
        return render(request, 'book/createbook.html', {'form': form})
    else:
        try:
            form = BookForm(request.POST, request.FILES)
            newbook = form.save(commit=False)
            newbook.user = request.user
            if form.is_valid():
                newbook.save()
                messages.success(request, 'Book saved!')
                return redirect('currentbooks')
        except ValueError:
            return render(request, 'book/createbook.html', {'form':BookForm()})


# Read
@login_required
def viewbook(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk, user=request.user)
    if request.method == 'GET':
        form = BookForm(instance=book)
        return render(request, 'book/viewbook.html', {'book':book, 'form':form})
    else:
        try:
            form = BookForm(request.POST, instance=book)
            form.save()
            return redirect('currentbooks')
        except ValueError:
            return render(request, 'book/viewbook.html', {'book':book, 'form':form, 'error':'Bad info'})
            
@login_required
def currentbooks(request):
    book_list = Book.objects.filter(user=request.user)
    paginator = Paginator(book_list, 2)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'book/currentbooks.html', {'page_obj': page_obj, 'book_list': book_list})

@login_required
def wanttoreadbooks(request):
    book_list = Book.objects.filter(user=request.user, status="Want To Read")
    paginator = Paginator(book_list, 2)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'book/wanttoread.html', {'page_obj': page_obj, 'book_list': book_list})
    
@login_required
def currentlyreading(request):
    book_list = Book.objects.filter(user=request.user, status="Currently Reading")
    paginator = Paginator(book_list, 2)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'book/currentlyreading.html', {'page_obj': page_obj, 'book_list': book_list})
    
@login_required
def read(request):
    book_list = Book.objects.filter(user=request.user, status="Read")
    paginator = Paginator(book_list, 2)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'book/read.html', {'page_obj': page_obj, 'book_list': book_list})


# Delete
@login_required
def deletebook(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk, user=request.user)
    if request.method == 'POST':
        book.delete()
        messages.info(request, 'Book deleted!')
        return redirect('currentbooks')
  
@login_required
def editbook(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    if request.method == 'GET':
        # Render the form
        form = BookForm(instance=book)
        return render(request, 'book/editbook.html', {'book':book, 'form':form})
    else:
        try:
            form = BookForm(request.POST, request.FILES, instance=book)
            if form.is_valid():
                form.save()
                messages.info(request, 'Your book has been edited.')
                return redirect('currentbooks')
        except ValueError:
            messages.error(request, 'Bad info.')
            return render(request, 'book/editbook.html', {'book':book, 'form':form})


# View without logging in
def viewonly(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    reviews = Review.objects.filter(book=book).order_by('-id')
    if request.method == 'GET':
        review_form = ReviewForm()
        return render(request, 'book/viewonly.html', {'book':book, 'reviews':reviews, 'review_form':review_form})
    else:
        try:
            review_form = ReviewForm(request.POST or None)
            if review_form.is_valid():
                content = request.POST.get('content')
                review = Review.objects.create(book=book, user=request.user, content=content)
                review.save()
                messages.success(request, 'Review posted.')
                return HttpResponseRedirect(book.get_absolute_url())
            return redirect('currentbooks')
        except ValueError:
            return render(request, 'book/viewonly.html', {'book':book, 'error':'Bad info'})
            
# Add genre class
class AddGenreView(CreateView):
    model = Genre
    template_name = 'book/genre.html'
    fields = '__all__'
    


