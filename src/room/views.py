from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from room.entities import Deck
from room.models import CardRoom
from .serializers import RoomSerializer, CardSerializer
from .utils import get_controller
from .utils import game_controller
from .forms import GameForm
import datetime
from django.utils import timezone


class Room(LoginRequiredMixin, TemplateView):
    template_name = "room/Room.html"

    def __init__(self):
        super().__init__()
        self.controller = get_controller()
        self.game = game_controller()

    def post(self, request, pk):
        card_room = get_object_or_404(CardRoom, pk=pk)

        if "Join" in request.POST:
            user = request.user
            try:
                self.controller.add_player(user, card_room)
            except ValueError:
                return redirect("the_room", pk=pk)

            players = list(card_room.players.all())
            players_count = self.controller.check_players_num(card_room)

            if players_count == 4:
                self.game.setup_room(card_room, Deck().cards)

            if players_count == 4 and card_room.status:
                content = {
                    "table_status": False,
                    "register": False,
                    "cancel": False,
                    "countdown": True,
                    "timer": "6",
                }
                return render(request, self.template_name, content)

            content = {
                "table_status": True,
                "players": players,
                "room_nr": pk,
                "cancel": True,
                "register": False,
            }
            return render(request, self.template_name, content)

        elif "Cancel" in request.POST:
            user = request.user
            self.controller.remove_player(user, card_room)

            players = card_room.players.all()
            content = {
                "table_status": True,
                "players": players,
                "room_nr": pk,
                "cancel": False,
                "register": True,
            }
            return render(request, self.template_name, content)

        elif "Post_Card" in request.POST:
            form = GameForm(request.POST)
            if form.is_valid():
                card = form.cleaned_data["input"]
                if self.game.check_card(card):
                    self.game.save_card(card, card_room)

                self.game.run(card_room, card)
                return redirect("the_room", pk=pk)

    def get(self, request, pk):
        form = GameForm()
        card_room = get_object_or_404(CardRoom, pk=pk)
        room_stats = self.game.repository.get_room_stats(card_room)
        players = list(card_room.players.all())
        players_count = self.controller.check_players_num(card_room)
        is_registered = self.controller.check_user(request.user, card_room)

        time_since_card_was_played = int((timezone.now() - room_stats.last_played_card).total_seconds())
        if time_since_card_was_played > 10:
            self.game.play_card_for_player(card_room, room_stats, players[room_stats.player_position])

        if card_room.status and players_count == 4:
            if self.game.players_cards_count(players) == 0:
                self.game.setup_room(card_room, Deck().cards)

            context = {
                # Players
                "player1": players[0],
                "player2": players[1],
                "player3": players[2],
                "player4": players[3],
                # GAME STATS
                "board": room_stats.board,
                "trump_card": room_stats.trump_card,
                "team_1_score": room_stats.team_one_score,
                "team_2_score": room_stats.team_two_score,
                # HTML ELEMENTS
                "table_status": False,
                "game_status": True,
                "register": False,
                "cancel": False,
                "countdown": False,
                "timer": "0",
                "form": form,
            }
        else:
            context = {
                "players": players,
                "room_nr": pk,
                "register": is_registered,
                "cancel": not is_registered,
                "countdown": False,
                "timer": "0",
                "table_status": card_room.status,
                "form": form,
            }

        return render(request, self.template_name, context)


class CardRooms(LoginRequiredMixin, ListView):
    model = CardRoom
    context_object_name = "rooms"
    template_name = "room/cardroom_list.html"


class RoomApiView(RetrieveAPIView):
    queryset = CardRoom.objects.all()
    serializer_class = RoomSerializer

    def patch(self, *args, **kwargs):
        card_room = self.get_object()
        serializer = CardSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        played_card = serializer.data["card"]
        game_controller().run(card_room, played_card)
        return Response(serializer.data)
