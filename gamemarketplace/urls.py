from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', include('marketplace.urls')),
    path('admin/', admin.site.urls),
]
