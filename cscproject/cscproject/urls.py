
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('accounts.urls')),
    path('portal/', include('portal.urls')),
    path('results/', include('result.urls')),
    path('course/', include('course.urls'))
]
