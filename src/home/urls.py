from django.urls import path
from room.views import CardRooms
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views


urlpatterns = [
    path("", views.HomeView.as_view(), name="home_page"),
    path("card_rooms", CardRooms.as_view(), name="card_rooms"),
] + staticfiles_urlpatterns()
