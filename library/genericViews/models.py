from django.db import models

# Create your models here.
class Booking(models.Model):
    bookname=models.CharField(max_length=100)
    authorname=models.CharField(max_length=100)
    category=models.CharField(max_length=50)
    count=models.CharField(max_length=10)
    callno=models.CharField(max_length=10)
    publication=models.CharField(max_length=100)
    section=models.CharField(max_length=100)

    def __str__(self):
        return self.bookname
