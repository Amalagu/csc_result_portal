import os
from django.db import models
from accounts.models import User
from .choicelists import TAG_CHOICES, GENRE_CHOICES
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.



class Genre(models.Model):
    name= models.CharField(max_length=50, choices=GENRE_CHOICES)

    def __str__(self):
        return self.name


for (x,y) in GENRE_CHOICES:
    Genre.objects.create(name=x)

class Tag(models.Model):
    name = models.CharField(max_length=50, choices=TAG_CHOICES)

    def __str__(self):
        return self.name
    


class Book(models.Model):
    LANGUAGE_CHOICES = (
        ('en', 'English'),
        ('fr', 'French'),
        ('de', 'German'),
        # Add more languages as needed
    )
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=300, default='default')
    author = models.CharField(max_length=120)
    publisher = models.CharField(max_length=120, default='default')
    isbn = models.CharField(max_length=100, blank=True, null=True)
    publication_year = models.IntegerField( blank=True, null=True,
        validators=[
            MinValueValidator(1000),
            MaxValueValidator(9999)
        ]
    )
    genre = models.ManyToManyField(Genre)
    tags = models.CharField(max_length=300, default='default')
    uploader = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    file = models.FileField(upload_to='uploads/')
    coverpage = models.FileField(blank=True, null=True, default='uploads/coverpages/manipulated.jpeg', upload_to='uploads/coverpages/')
    thumbnail = models.FileField(blank=True, null=True, default='uploads/thumbnails/manipulated.jpeg', upload_to='uploads/thumbnails/')
    filepath = models.TextField(max_length=300, blank=True, null=True)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default='en')
    stars = models.IntegerField(blank=True, null=True, default=0)

    def delete(self, *args, **kwargs):
        # Delete the associated file from the file manager
        if self.filepath:
            try:
                file_path = os.path.normpath(self.filepath)
                if os.path.exists(file_path):
                    os.remove(file_path)
                    print("FILE DELETED EXISTS")
            except Exception as e:
                print(str(e))
                pass

        # Call the parent class's delete method to delete the model instance
        super().delete(*args, **kwargs)




class FavoriteBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    starred_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str( str(self.user) + " " + self.book.title)