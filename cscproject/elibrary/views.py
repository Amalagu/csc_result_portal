from django.shortcuts import render, redirect
from .models import Genre, Tag
from django.contrib.auth.decorators import login_required
from .forms import BookForm
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Book, FavoriteBook
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
import fitz  # PyMuPDF
from PIL import Image
import io
from pathlib import Path
import os
from django.core.files.base import ContentFile
from django.conf import settings
#import pikepdf

BASE_DIR = Path(__file__).resolve().parent.parent
# Create your views here.

def student_lib_home(request):
    return render(request, 'elibrary/lib-student-home.html')

def student_lib_book_details(request, pk):
    book = Book.objects.get(id=pk)

    context = {
        'book': book
    }
    return render(request, 'elibrary/lib-student-book-details.html', context)


def student_lib_book_read(request, pk):
    return render(request, 'elibrary/lib-student-book-read.html')


def student_lib_search_result(request):
    return render(request, 'elibrary/lib-student-search-results.html')

""" def staff_lib_home(request):
    return render(request, 'elibrary/lib-staff-home.html') """





@login_required
def staff_lib_home(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.uploader = request.user
            uploaded_file = form.cleaned_data['file']
            file_extension = uploaded_file.name.split('.')[-1].lower()
            if file_extension == 'pdf':
                # Save the book object
                book.save()

                # Save cover page and thumbnail images
                pdf_document = fitz.open(book.file.path)
                cover_page = pdf_document[0]
                cover_page_image = cover_page.get_pixmap()

                # Save cover page image
                cover_page_save_path = os.path.join(settings.MEDIA_ROOT, 'uploads/coverpages/temp/', f'{book.id}_cover.png')
                cover_page_image.save(cover_page_save_path)

                # Convert cover page image to thumbnail
                image = Image.open(cover_page_save_path)
                image.thumbnail((100, 75))
                #image_content = ContentFile(image.tobytes())
                # Save the image content to a BytesIO object
                image_io = io.BytesIO()
                image.save(image_io, format='PNG')
                image_content = ContentFile(image_io.getvalue())

                # Save thumbnail image
                thumbnail_save_path = os.path.join(settings.MEDIA_ROOT, 'uploads/thumbnails/', f'{book.id}_thumbnail.png')
                #image.save(thumbnail_save_path)
                #thumbnail_content = ContentFile(image.tobytes())
                thumbnail_content = ContentFile(image_io.getvalue())

                # Update book object with file paths
                book.coverpage.save(f"{book.id}_cover.png", image_content, save=False)
                book.thumbnail.save(f"{book.id}_thumbnail.png", thumbnail_content, save=False)
                #book.coverpage.name = f'uploads/coverpages/{book.id}_cover.png'
                #book.thumbnail.name = f'uploads/thumbnails/{book.id}_thumbnail.png'
                book.save()

                return redirect('staff_lib_book_detail', pk=book.pk)
            else:
                error_message = 'Please upload only a PDF document!'
                return render(request, 'upload.html', {'form': form, 'error_message': error_message})
    else:
        form = BookForm()
    return render(request, 'elibrary/lib-staff-home.html', {'form': form})



""" @login_required
def staff_lib_home(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.uploader = request.user
            uploaded_file = form.cleaned_data['file']
            file_extension = uploaded_file.name.split('.')[-1].lower()
            if file_extension == 'pdf':
                # Save the book object
                book.save()

                # Save cover page and thumbnail images
                pdf_document = fitz.open(book.file.path)
                cover_page = pdf_document[0]
                cover_page_image = cover_page.get_pixmap()

                # Save cover page image
                cover_page_save_path = os.path.join(settings.MEDIA_ROOT, 'uploads/coverpages/temp/', f'{book.id}_cover.png')
                cover_page_image.save(cover_page_save_path)

                # Convert cover page image to thumbnail
                image = Image.open(cover_page_save_path)
                image.thumbnail((100, 75))
                image_content = ContentFile(image.tobytes())

                # Save the image content to a BytesIO object
                #image_io = io.BytesIO()
                #image.save(image_io, format='PNG')
                #image_content = ContentFile(image_io.getvalue())

                # Save thumbnail image
                thumbnail_save_path = os.path.join(settings.MEDIA_ROOT, 'uploads/thumbnails/', f'{book.id}_thumbnail.png')
                #image.save(thumbnail_save_path)
                thumbnail_content = ContentFile(image.tobytes())
                #thumbnail_content = ContentFile(image_io.getvalue())

                # Update book object with file paths
                book.coverpage.save(f"{book.id}_cover.png", image_content, save=False)
                book.thumbnail.save(f"{book.id}_thumbnail.png", thumbnail_content, save=False)
                #book.coverpage.name = f'uploads/coverpages/{book.id}_cover.png'
                #book.thumbnail.name = f'uploads/thumbnails/{book.id}_thumbnail.png'
                book.save()

                return redirect('staff_lib_book_detail', pk=book.pk)
            else:
                error_message = 'Please upload only a PDF document!'
                return render(request, 'upload.html', {'form': form, 'error_message': error_message})
    else:
        form = BookForm()
    return render(request, 'elibrary/lib-staff-home.html', {'form': form}) """






""" def staff_lib_home(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        #form.publication_year = int(form.publication_year)
        print(form.errors)
        print(request.POST)
        if form.is_valid():
            book = form.save()
            book.uploader = request.user
            # Ensure only PDF documents are allowed
            uploaded_file = form.cleaned_data['file']
            file_extension = uploaded_file.name.split('.')[-1].lower()
            if file_extension == 'pdf':
                print("THIIS IS IT ", book.file.path)
                pdf_document = fitz.open(book.file.path)
                cover_page = pdf_document[0]
                cover_page_image = cover_page.get_pixmap()
                
                cover_page_save_path = os.path.join(settings.MEDIA_ROOT, f'uploads/coverpages/{uploaded_file.name}_cover.png')
                #cover_page_save_path = f'/uploads/coverpages/{uploaded_file.name}_cover.png'
                cover_page_image.save(cover_page_save_path)
                
                # Convert Pixmap to image object
                #img_buffer = io.BytesIO()
                #cover_page_image.save(img_buffer)
                #img_buffer.seek(0)
                image = Image.open(cover_page_save_path)

                # For thumbnail
                image.thumbnail((100, 75))
                thumbnail_save_path = os.path.join(settings.MEDIA_ROOT, f'uploads/thumbnails/{uploaded_file.name}_cover.png')
                #thumbnail_save_path = f'/uploads/thumbnails/{uploaded_file.name}_cover.png'
                image.save(thumbnail_save_path)
                # Save the images
                book.coverpage.save(uploaded_file.name + "_cover.png", save=False)
                book.thumbnail.save(uploaded_file.name + "_thumbnail.png", image, save=False)
                
                book.filepath = uploaded_file.name
                book.save()
                return redirect('staff_lib_book_detail', pk=book.pk)
            else:
                error_message = 'Please upload only a PDF document!'
                return render(request, 'upload.html', {'form': form, 'error_message': error_message})
            return redirect('staff_lib_book_detail', pk=book.pk)
            #book_url = request.build_absolute_uri(book.file.url)
            #print("THIS IS REQUEST BOOK URL ", book_url) #http://127.0.0.1:8000/media/uploads/Screenshot_1_wcSGcWy.png
            #print("THIS IS REQUEST BOOK URL ", book.file.url) #/media/uploads/Screenshot_2_huTU50u.png
           
    else:
        form = BookForm()
    return render(request, 'elibrary/lib-staff-home.html', {'form': form}) """



def staff_lib_book_detail(request, pk):
    book = Book.objects.get(id=pk)

    context = {
        'book': book
    }
    return render(request, 'elibrary/lib-staff-book-details.html', context)

def staff_lib_book_read(request, pk):
    return render(request, 'elibrary/lib-staff-book-read.html')



def star_book(request, pk):
    if request.method == 'POST':
        book = get_object_or_404(Book, id=pk)
        favourite, created = FavoriteBook.objects.get_or_create(book=book, user=request.user)
        if created:
            book.stars += 1
            book.save()
            return HttpResponse("Book has been successfully starred.", status=200)
        else:
            favourite.delete()
            book.stars -= 1
            book.save()
            return HttpResponse("Book is unstarred.", status=200)
    else:
        pass


""" 
def staff_lib_upload_book(request):
    return render(request, 'elibrary/lib-staff-upload-book.html') """








@login_required
def staff_lib_upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.uploader = request.user
            uploaded_file = request.FILES['file']
            if uploaded_file.name.endswith('.pdf'):
                # Save the uploaded PDF to a temporary file
                temp_pdf_path = os.path.join('temp', uploaded_file.name)
                with open(temp_pdf_path, 'wb+') as f:
                    for chunk in uploaded_file.chunks():
                        f.write(chunk)

                # Open the PDF with fitz
                pdf_document = fitz.open(temp_pdf_path)
                cover_page = pdf_document[0]
                cover_page_image = cover_page.get_pixmap()

                # Save the cover page image
                cover_page_save_path = os.path.join('uploads', 'coverpages', f'{uploaded_file.name}_cover.png')
                cover_page_image.save(cover_page_save_path)

                # Convert Pixmap to image object
                img_buffer = io.BytesIO()
                cover_page_image.save(img_buffer, format='PNG')
                img_buffer.seek(0)
                image = Image.open(img_buffer)

                # Create and save thumbnail
                image.thumbnail((100, 75))
                thumbnail_save_path = os.path.join('uploads', 'thumbnails', f'{uploaded_file.name}_thumbnail.png')
                image.save(thumbnail_save_path)

                # Save the images in the model
                book.cover_page.save(f'{uploaded_file.name}_cover.png', ContentFile(img_buffer.getvalue()), save=False)
                thumbnail_buffer = io.BytesIO()
                image.save(thumbnail_buffer, format='PNG')
                thumbnail_buffer.seek(0)
                book.thumbnail.save(f'{uploaded_file.name}_thumbnail.png', ContentFile(thumbnail_buffer.getvalue()), save=False)

                # Clean up the temporary PDF file
                #os.remove(temp_pdf_path)

                book.filepath = uploaded_file.name
                book.save()
                return redirect('staff_lib_book_detail', pk=book.pk)
            else:
                form.add_error('file', 'Please upload only a PDF document.')
    else:
        form = BookForm()
    return render(request, 'elibrary/lib-staff-upload-book.html', {'form': form})












""" from django.core.files.base import ContentFile

# ... [rest of your code] ...

# For cover page
cover_page_image.save(cover_page_save_path)

# Convert Pixmap to image object and create a ContentFile for saving
image = Image.open(cover_page_save_path)
image_content = ContentFile(image.tobytes())

# For thumbnail
image.thumbnail((100, 75))
thumbnail_save_path = os.path.join(settings.MEDIA_ROOT, f'uploads/thumbnails/{uploaded_file.name}_cover.png')
image.save(thumbnail_save_path)
thumbnail_content = ContentFile(image.tobytes())

# Save the images with the content
book.coverpage.save(uploaded_file.name + "_cover.png", image_content, save=False)
book.thumbnail.save(uploaded_file.name + "_thumbnail.png", thumbnail_content, save=False)

# ... [rest of your code] ...
 """


#############################################################################################
#                                                                                           #
#                               API(s)                                                      #
#                                                                                           #
#############################################################################################


@api_view(['GET'])
def books_api(request):
    user = request.user
    users_favorite_books = FavoriteBook.objects.filter(user=user).order_by('-starred_at')
    associated_books = [favorite.book for favorite in users_favorite_books]
    book_type = request.GET.get('type', None)
    
    if book_type == 'recommended':
        books = Book.objects.all()
    elif book_type == 'popular':
        books = Book.objects.all().order_by("-stars")
    elif book_type == 'my_books':
        books = associated_books
    elif book_type == 'uploaded_books':
        user = request.user
        books = Book.objects.filter(uploader=user)
    else:
        # If no specific type is requested, return all books
        books = Book.objects.all()
    
    # Serialize the queryset
    serializer = BookSerializer(books, many=True)
    data = serializer.data
    # Mark favorite books
    for book_data in data:
        book_data['is_favorite'] = book_data['id'] in [book.id for book in associated_books]
    return Response(serializer.data, status=status.HTTP_200_OK)
