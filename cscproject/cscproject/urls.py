
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
import portal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('portal/', include('portal.urls')),
    path('results/', include('result.urls')),
    path('course/', include('course.urls')),
    path('elibrary/', include('elibrary.urls')),
    path("", portal.views.home_view)
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
