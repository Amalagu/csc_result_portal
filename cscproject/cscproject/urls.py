
from django.contrib import admin
from django.urls import path, include
import portal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('portal/', include('portal.urls')),
    path('results/', include('result.urls')),
    path('course/', include('course.urls')),
    path("", portal.views.home_view)
]
