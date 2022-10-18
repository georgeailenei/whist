from django.urls import path
from . import views


urlpatterns = [
    path('card-rooms', views.CardRooms.as_view(), name='CardRooms'),
]
