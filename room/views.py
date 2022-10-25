from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView, ListView
from room.models import CardRoom
from .utils import get_controller
from django.contrib.auth.mixins import LoginRequiredMixin


class Room(LoginRequiredMixin, TemplateView):
    template_name = 'room/Room.html'

    def __init__(self):
        super().__init__()
        self.controller = get_controller()

    def post(self, request, pk):
        card_room = get_object_or_404(CardRoom, pk=pk)

        if 'Join' in request.POST:
            user = request.user
            self.controller.add_player(user, card_room)
            cancel = True
            register = False
            players = self.controller.get_players_names(card_room)

            content = {
                'players': players,
                'room_nr': pk,
                'cancel': cancel,
                'register': register,
            }
            return render(request, self.template_name, content)

        elif 'Cancel' in request.POST:
            user = request.user
            cancel = False
            register = True
            self.controller.remove_player(user, card_room)
            players = self.controller.get_players_names(card_room)

            content = {
                'players': players,
                'room_nr': pk,
                'cancel': cancel,
                'register': register,
            }
            return render(request, self.template_name, content)

    def get(self, request, pk):
        card_room = get_object_or_404(CardRoom, pk=pk)
        players = self.controller.get_players_names(card_room)

        register = self.controller.check_user(request.user, card_room)
        cancel = not register

        players_count = self.controller.check_players_num(card_room)
        message = ""

        if players_count == 4:
            register = False
            cancel = False
            message = "The game will start shortly"

        content = {
            'players': players,
            'room_nr': pk,
            'register': register,
            'cancel': cancel,
            'message': message,
        }
        return render(request, self.template_name, content)


class CardRooms(LoginRequiredMixin, ListView):
    model = CardRoom
    context_object_name = 'rooms'
    template_name = 'room/cardroom_list.html'
