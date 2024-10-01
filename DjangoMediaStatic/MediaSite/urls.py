from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import CreateMedia, ListMedia, MediaDetails

urlpatterns = [
    path('new_media/', CreateMedia.as_view(), name='create_media'),
    path('', ListMedia.as_view(), name='home'),
    path('<int:pk>/', MediaDetails.as_view(), name='detail_media')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


