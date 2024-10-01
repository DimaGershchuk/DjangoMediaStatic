from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import MyMediaCreateView, MyMediaDetailView, MyMediaListView

urlpatterns = [
    path('new_media/', MyMediaCreateView.as_view(), name='create_media'),
    path('', MyMediaListView.as_view(), name='home'),
    path('<int:pk>/', MyMediaDetailView.as_view(), name='detail_media')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


