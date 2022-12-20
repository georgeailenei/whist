from django.urls import path
from . import views


urlpatterns = [
    path("card_rooms/", views.CardRooms.as_view(), name="card_rooms_list"),
    path("card_rooms/<int:pk>/", views.Room.as_view(), name="the_room"),
    path("card_rooms/<int:pk>/game", views.Game.as_view(), name="game"),

    path("rooms/<int:pk>/", views.RoomApiView.as_view(), name="room_api_view"),
]
