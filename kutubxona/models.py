from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=512)
    author = models.CharField(max_length=512)
    description = models.TextField()
    image = models.URLField(max_length=512,blank=True,null=True)


class Review(models.Model):
    text = models.TextField()
    rating = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class User(models.Model):
    name = models.CharField(max_length=512)
    email = models.EmailField()
    password = models.CharField(max_length=512)



