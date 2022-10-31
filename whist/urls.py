from django.urls import path
from . import views


urlpatterns = [
    path('test/', views.GamesView.as_view(), name='games'),
    path('test/whist/', views.WhistView.as_view(), name='whist'),
]
