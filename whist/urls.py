from django.urls import path
from . import views


urlpatterns = [
    path('', views.GamesView.as_view(), name='games'),
    path('whist', views.WhistView.as_view(), name='whist'),
]
