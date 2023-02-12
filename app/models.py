from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Book(models.Model):
    book_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book_name = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    book_publisher = models.CharField(max_length=100)
    book_price = models.IntegerField()
    book_status = models.BooleanField()
    book_image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.book_name
    
class Vistors(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)