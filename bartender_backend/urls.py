from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from .views import index

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', index),
    path('admin/',admin.site.urls),
    path('api/', include('bartender_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)