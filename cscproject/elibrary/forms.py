""" from django import forms
from .models import Book, Genre

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'isbn', 'publication_year', 'genre', 'tags', 'file')
        widgets = {
            'publication_year': forms.DateInput(attrs={'type': 'date'}),
        } """
        
""" def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['genre'] = forms.ModelMultipleChoiceField(Genre.objects.all()) """

from django import forms
from .models import Book, Genre

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'subtitle', 'author', 'publisher', 'isbn', 'publication_year', 'genre', 'tags', 'file', 'language')

    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(attrs={'class': 'input w-full', 'id': 'title'})
    )

    subtitle = forms.CharField(
        label='Subtitle',
        widget=forms.TextInput(attrs={'class': 'input w-full', 'id': 'subtitle'})
    )

    author = forms.CharField(
        label='Author',
        widget=forms.TextInput(attrs={'class': 'input w-full', 'id': 'author'})
    )

    publisher = forms.CharField(
        label='Publisher',
        widget=forms.TextInput(attrs={'class': 'input w-full', 'id': 'publisher'})
    )

    isbn = forms.CharField(
        label='ISBN',
        widget=forms.TextInput(attrs={'class': 'input w-full', 'id': 'isbn'})
    )

    publication_year = forms.IntegerField(
        label='Year of Publication',
        widget=forms.NumberInput(attrs={'class': 'input w-full', 'id': 'publicationYear'})
    )

    genre = forms.ModelMultipleChoiceField(
        label='Genre',
        queryset=Genre.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'w-full h-10 -mt-[0.23rem]'})
    )

    tags = forms.CharField(
        label='Tags',
        widget=forms.TextInput(attrs={'class': 'input w-full', 'id': 'tags'})
    )

    file = forms.FileField(
        label='Upload Document',
        widget=forms.FileInput(attrs={'class': 'input w-full', 'id': 'doc'})
    )

    language = forms.ChoiceField(
        label='Language',
        choices=Book.LANGUAGE_CHOICES,
        widget=forms.Select(attrs={'class': 'w-full h-10 -mt-[0.23rem]'})
    )
