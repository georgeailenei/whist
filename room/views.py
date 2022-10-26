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
            try:
                self.controller.add_player(user, card_room)
            except ValueError:
                return redirect('the_room', pk=pk)

            players = self.controller.get_players_names(card_room)
            content = {
                'table_status': True,
                'players': players,
                'room_nr': pk,
                'cancel': True,
                'register': False,
            }
            return render(request, self.template_name, content)

        elif 'Cancel' in request.POST:
            user = request.user
            self.controller.remove_player(user, card_room)
            players = self.controller.get_players_names(card_room)
            content = {
                'table_status': True,
                'players': players,
                'room_nr': pk,
                'cancel': False,
                'register': True,
            }
            return render(request, self.template_name, content)

    def get(self, request, pk):
        card_room = get_object_or_404(CardRoom, pk=pk)
        players = self.controller.get_players_names(card_room)
        card_room_status = self.controller.get_room_status(card_room)
        print(card_room_status)
        register = self.controller.check_user(request.user, card_room)
        cancel = not register

        players_count = self.controller.check_players_num(card_room)
        countdown = False
        seconds = "0"

        if players_count == 4:
            self.controller.change_status_to_false(card_room)
            register, cancel, countdown = False, False, True
            seconds = "6"
            content = {
                'table_status': False,
                'register': register,
                'cancel': cancel,
                'countdown': countdown,
                'timer': seconds,
            }
            return render(request, self.template_name, content), redirect('the_game')

        content = {
            'players': players,
            'room_nr': pk,
            'register': register,
            'cancel': cancel,
            'countdown': countdown,
            'timer': seconds,
            'table_status': card_room_status,
        }
        return render(request, self.template_name, content)


class CardRooms(LoginRequiredMixin, ListView):
    model = CardRoom
    context_object_name = 'rooms'
    template_name = 'room/cardroom_list.html'


class TheGame(LoginRequiredMixin, TemplateView):
    template_name = 'room/game.html'

    def get(self, request):
        return render(request, self.template_name)
