from django.db import models
from accounts.models import User
# Create your models here.



class Genre(models.Model):
    name= models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    


class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=120)
    isbn = models.CharField(max_length=100)
    publication_year = models.DateField()
    genre = models.ManyToManyField(Genre)
    tags = models.ManyToManyField(Tag)
    uploader = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)





