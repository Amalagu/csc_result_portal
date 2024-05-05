from django.contrib import admin
from .models import Book, Tag, Genre, FavoriteBook

# Register your models here.
admin.site.register(Book)
admin.site.register(Tag)
admin.site.register(Genre)
admin.site.register(FavoriteBook)