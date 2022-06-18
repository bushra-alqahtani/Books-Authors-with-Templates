from django.db import models

# Create your models here.

from django.db import models
from books_authors_app.models import *

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    desc=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Auther(models.Model):
    first_name = models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    desc=models.TextField()
    notes=models.TextField(default="")
    books= models.ManyToManyField(Book, related_name="authers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)