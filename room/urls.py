from django.urls import path
from . import views


urlpatterns = [
    path('card-rooms/<pk>', views.CardRooms.as_view(), name='card_rooms'),
]
