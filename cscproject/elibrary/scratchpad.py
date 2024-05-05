import fitz  # PyMuPDF
from PIL import Image


pdf_file = "pdf_file.pdf"
pdf_document = fitz.open(pdf_file)
first_page = pdf_document[0]
pix = first_page.get_pixmap()
image_path = "output_image.png"
pix.save(image_path)
image = Image.open(image_path)
image.thumbnail((100, 100))  # Define the size of your thumbnail
thumbnail_path = "thumbnail_image.png"
image.save(thumbnail_path)
pdf_document.close()
















                        <div  class="h-[85%] overflow-y-scroll">
                            <div class="text-center font-bold">Upload Book</div>
                            <hr>
                            <form class="w-full grid gap-3 md:grid-cols-2" method="post" enctype="multipart/form-data">
                                {{ error_message }}
                                {% csrf_token %}
                                <div>
                                    <label for="id_title" class="text-sm text-[--secondary-800] font-bold">Title</label>
                                    {{ form.title }}
                                </div>

                                <div>
                                    <label for="id_subtitle"
                                        class="text-sm text-[--secondary-800] font-bold">Subtitle</label>
                                    {{ form.subtitle }}
                                </div>

                                <div>
                                    <label for="id_author"
                                        class="text-sm text-[--secondary-800] font-bold">Author</label>
                                    {{ form.author }}
                                </div>

                                <div>
                                    <label for="id_publication_year"
                                        class="text-sm text-[--secondary-800] font-bold">Year of Publication</label>
                                    {{ form.publication_year }}
                                </div>

                                <div>
                                    <label for="id_publisher"
                                        class="text-sm text-[--secondary-800] font-bold">Publisher</label>
                                    {{ form.publisher }}
                                </div>

                                <div class="select" style="margin: 0;">
                                    <label for="id_language"
                                        class="text-sm text-[--secondary-800] font-bold">Language</label>
                                    {{ form.language }}
                                </div>

                                <div>
                                    <label for="id_tags" class="text-sm text-[--secondary-800] font-bold">Tags</label>
                                    {{ form.tags }}
                                </div>

                                <div class="select" style="margin: 0;">
                                    <label for="id_genre">Genre</label>
                                    <select name="genre" id="id_genre" class="w-full h-10 -mt-[0.23rem]">
                                        <option value="">Select Genre</option>
                                        {% for genre in form.genre.field.queryset %}
                                        <option value="{{ genre.pk }}">{{ genre.name }}</option>
                                        {% endfor %}
                                    </select>
                                </div>

                                <div>
                                    <label for="id_isbn" class="text-sm text-[--secondary-800] font-bold">ISBN</label>
                                    {{ form.isbn }}
                                </div>

                                <div class="file-input" style="margin: 0;">
                                    <label for="id_file" class="text-sm text-[--secondary-800] font-bold">Upload
                                        Document</label>
                                    {{ form.file }}
                                </div>

                                <div class="grid items-end">
                                    <button type="submit" style="background-color: green; color: white;"
                                        class="w-full h-10 font-semibold hover:bg-[--primary-600] transition-colors">Submit</button>
                                </div>


                            </form>

                            

                        </div>





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



 from django.core.files.base import ContentFile

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
                cover_page_save_path = os.path.join(settings.MEDIA_ROOT, 'uploads/coverpages/', f'{book.id}_cover.png')
                cover_page_image.save(cover_page_save_path)

                # Convert cover page image to thumbnail
                thumbnail_image = cover_page_image.copy()
                thumbnail_image.thumbnail((100, 75))
                
                # Save thumbnail image
                thumbnail_save_path = os.path.join(settings.MEDIA_ROOT, 'uploads/thumbnails/', f'{book.id}_thumbnail.png')
                thumbnail_image.save(thumbnail_save_path)

                # Update book object with file paths
                book.coverpage.save(f"{book.id}_cover.png", ContentFile(cover_page_image.tobytes()), save=False)
                book.thumbnail.save(f"{book.id}_thumbnail.png", ContentFile(thumbnail_image.tobytes()), save=False)
                book.save()

                return redirect('staff_lib_book_detail', pk=book.pk)
            else:
                error_message = 'Please upload only a PDF document!'
                return render(request, 'upload.html', {'form': form, 'error_message': error_message})
    else:
        form = BookForm()
    return render(request, 'elibrary/lib-staff-home.html', {'form': form})
