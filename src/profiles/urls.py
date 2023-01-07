from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('profile/', views.user_profile_view)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


