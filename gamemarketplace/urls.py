from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('marketplace.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('api/', include('api.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
