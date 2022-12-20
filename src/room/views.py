from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from room.models import CardRoom
from .serializers import RoomSerializer, CardSerializer
from .utils import get_controller
from .utils import game_controller
from django.utils import timezone


class Game(LoginRequiredMixin, TemplateView):
    template_name = "room/game.html"


class Room(LoginRequiredMixin, TemplateView):
    template_name = "room/room.html"

    def __init__(self):
        super().__init__()
        self.controller = get_controller()
        self.game = game_controller()

    def post(self, request, pk):
        card_room = get_object_or_404(CardRoom, pk=pk)
        user = request.user

        if "Join" in request.POST:
            try:
                self.controller.add_player(user, card_room)
            except ValueError:
                return redirect("the_room", pk=pk)
        elif "Cancel" in request.POST:
            self.controller.remove_player(user, card_room)

        return redirect("the_room", pk=pk)

    def get(self, request, pk):
        card_room = get_object_or_404(CardRoom, pk=pk)
        players = list(card_room.players.all())
        players_count = self.controller.check_players_num(card_room)
        is_registered = self.controller.check_user(request.user, card_room)

        if players_count == 4 and card_room.game_status:
            content = {
                "players": players,
                "room_nr": pk,
                "table_status": True,
                "register": is_registered,
                "cancel": not is_registered,
                "countdown": True,
                "timer": "6",
                "is_room_full": False,
            }
            print("ceva")
            return render(request, self.template_name, content)
        else:
            content = {
                "players": players,
                "room_nr": pk,
                "table_status": True,
                "register": is_registered,
                "cancel": not is_registered,
                "countdown": False,
                "timer": "0",
                "is_room_full": True,
            }
            return render(request, self.template_name, content)


class CardRooms(LoginRequiredMixin, ListView):
    model = CardRoom
    context_object_name = "rooms"
    template_name = "room/cardroom_list.html"


class RoomApiView(RetrieveAPIView):
    queryset = CardRoom.objects.all()
    serializer_class = RoomSerializer

    def get(self, *args, **kwargs):
        card_room = self.get_object()
        room_stats = card_room.stats
        time_since_card_was_played = (timezone.now() - room_stats.last_played_card).total_seconds()
        if time_since_card_was_played > 0.01:
            game_controller().play_card_for_player(card_room, room_stats, card_room.players.all()[room_stats.player_position])
        return super().get(*args, **kwargs)

    def patch(self, *args, **kwargs):
        card_room = self.get_object()
        serializer = CardSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        played_card = serializer.data["card"]

        game_controller().run(card_room, played_card)
        return Response(serializer.data)
