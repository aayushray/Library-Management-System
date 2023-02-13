from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
import uuid

# Create your models here.

class Book(models.Model):
    book_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book_name = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    book_publisher = models.CharField(max_length=100)
    book_price = models.IntegerField()
    book_image = models.ImageField(upload_to='images')
    is_issued = models.BooleanField(default = False)

    def __str__(self):
        return self.book_name
    
class Visitor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length = 100)
    full_name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    number_of_books = models.IntegerField(default = 0,null = True)

    def __str__(self):
        return self.full_name

def get_return_date():
    return datetime.today() + timedelta(days = 30)

class Book_Issue(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    book_name = models.ForeignKey(Book, on_delete = models.CASCADE)
    issue_date = models.DateField(auto_now = True)
    due_date = models.DateField(default = get_return_date)

    def __str__(self):
        return self.user