
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mp.urls')),
    # For the authentication
    path('accounts/', include('django.contrib.auth.urls')), 
]
