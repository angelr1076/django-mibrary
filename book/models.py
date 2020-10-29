from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

        
class Genre(models.Model):
    name = models.CharField(max_length=100)
    
    def get_absolute_url(self):
        return reverse('home')
    
    def __str__(self):
        return f'{self.name}'

class Book(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    book_img = models.ImageField(null=True, blank=True, upload_to="images/book/")
    summary = RichTextField(blank=True, null=True)
    isbn = models.CharField(blank=True, null=True, max_length=25)
    genre = models.CharField(blank=True, null=True, max_length=100, default='Fiction')
    status = models.CharField(blank=True, null=True, max_length=100, default='Want to read')
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Redirect for comments
    def get_absolute_url(self):
        return reverse('viewonly', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.title} by {self.author}'
        

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=250)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.book.title} {self.user.username}'
   
        
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    website_url = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return str(self.user)