from django.forms import ModelForm
from django import forms
from .models import *


# Default statuses
book_read = [('Want To Read', 'Want To Read'), ('Currently Reading', 'Currently Reading'), ('Read', 'Read'),]
status_list = []

for item in book_read:
    status_list.append(item)


# Categories for BookForm genre widget
categories = Genre.objects.all().values_list('name', 'name')
category_list = []

for item in categories:
    category_list.append(item)


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('author', 'title', 'genre', 'status', 'book_img', 'summary', 'isbn')
        ordering = ['-id']
        labels = {'book_img': ('Book Cover'), 'isbn': ('ISBN')}
        
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.Select(choices=category_list, attrs={'class': 'form-control'}),
            'status': forms.Select(choices=status_list, attrs={'class': 'form-control'}),
            'summary': forms.Textarea(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ViewOnlyForm(ModelForm):
    class Meta:
        model = Book
        fields = ('author', 'title', 'summary', 'isbn')
        
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'style':'background:none; border:none'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'style':'background:none; border:none'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'readonly': 'readonly', 'style':'background:none; border:none'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'style':'background:none; border:none'}),
        }
        
        
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ('content',)
        labels = {'content': ('Review'),}
        
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'cols': 40, 'style': 'width:50%;'}),
        }