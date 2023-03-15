from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from room.models import CardRoom
from .entities import Deck
from .serializers import RoomSerializer, CardSerializer, ChoiceSerializer, PlayerSerializer
from .utils import get_controller
from .utils import game_controller
from django.utils import timezone
from profiles.controllers.rank_controller import ranking
from .repos.room_stats import RoomStats


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
        players_count = self.controller.check_players_num(card_room)
        user = request.user
        ranking(user)

        if "Join" in request.POST:
            try:
                self.controller.add_player(user, card_room)
            except ValueError:
                return redirect("the_room", pk=pk)
            if players_count == 4:
                card_room.game_status = True

        elif "Cancel" in request.POST:
            self.controller.remove_player(user, card_room)
        return redirect("the_room", pk=pk)

    def get(self, request, pk):
        card_room = get_object_or_404(CardRoom, pk=pk)
        stats = RoomStats()
        room_stats = stats.get_room_stats(card_room)
        players = list(card_room.players.all())
        players_count = self.controller.check_players_num(card_room)
        is_registered = self.controller.check_user(request.user, card_room)

        if players_count == 4 and card_room.game_status:
            return redirect("game", pk=pk)
        elif players_count == 4 and not card_room.game_status and room_stats.team_one_score == 0 and room_stats.team_one_score == 0:
            return redirect("game", pk=pk)
        elif not card_room.game_status:
            content = {
                "players": players,
                "room_nr": pk,
                "room_status": True,
                "register": is_registered,
                "cancel": not is_registered,
            }
            return render(request, self.template_name, content)


class CardRooms(LoginRequiredMixin, ListView):
    model = CardRoom
    template_name = "room/cardroom_list.html"

    def __init__(self):
        super().__init__()
        self.controller = get_controller()

    def post(self, request):
        if 'Join' in request.POST:
            room_id = request.POST['Join']
            card_room = get_object_or_404(CardRoom, pk=room_id)
            players_count = self.controller.check_players_num(card_room)
            user = request.user

            try:
                self.controller.add_player(user, card_room)
            except ValueError:
                return redirect('game', pk=room_id)
            if players_count == 3:
                return redirect('the_room', pk=room_id)
            return redirect('game', pk=room_id)

    def get(self, request):
        the_rooms = CardRoom.objects.all()
        players_count = [len(room.players.all()) for room in the_rooms]
        rooms = zip(the_rooms, players_count)

        content = {
            'rooms': rooms,
        }
        return render(request, self.template_name, content)


class RoomApiView(RetrieveAPIView):
    queryset = CardRoom.objects.all()
    serializer_class = RoomSerializer

    def get(self, *args, **kwargs):
        card_room = self.get_object()
        room_stats = card_room.stats

        if not card_room.game_status and len(card_room.players.all()) == 4:
            game_controller().setup_room(card_room, Deck().cards)
        elif not card_room.game_status and len(card_room.players.all()) == 4 and room_stats.team_one_score == 0 and room_stats.team_one_score == 0:
            card_room.game_status = True
            card_room.save()
            game_controller().setup_room(card_room, Deck().cards)

        if card_room.game_status:
            time_since_card_was_played = (timezone.now() - room_stats.last_played_card).total_seconds()
            if game_controller().game_first_hand(card_room.players.all()) and card_room.game_status:
                if time_since_card_was_played - 5 > 10:
                    game_controller().play_card_for_player(card_room, room_stats, card_room.players.all()[room_stats.player_position])
            elif time_since_card_was_played > 5 and card_room.game_status:
                game_controller().play_card_for_player(card_room, room_stats, card_room.players.all()[room_stats.player_position])
        return super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        card_room = self.get_object()
        serializer = ChoiceSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        choice = serializer.data["choice"]

        serializerTwo = PlayerSerializer(data=self.request.data)
        serializerTwo.is_valid(raise_exception=True)
        player = serializerTwo.data["player"]

        if card_room.game_status:
            game_controller().run(card_room, "", choice, player)
        return Response(serializer.data)

    def patch(self, *args, **kwargs):
        card_room = self.get_object()
        serializer = CardSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        played_card = serializer.data["card"]
        if card_room.game_status:
            game_controller().run(card_room, played_card, "", "")
        return Response(serializer.data)
