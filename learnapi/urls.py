from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Connection to API-URLS Paths 
    path('api/', include('myapp.urls')),
]
