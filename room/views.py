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

            card_room_status = self.controller.get_room_status(card_room)
            players = self.controller.get_players_names(card_room)
            players_count = self.controller.check_players_num(card_room)

            if players_count == 4 and card_room_status:
                self.controller.change_status_to_false(card_room)
                content = {
                    'table_status': False,
                    'register': False,
                    'cancel': False,
                    'countdown': True,
                    'timer': "6",
                }
                return render(request, self.template_name, content)

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
        # ROOM & PLAYERS & COUNT
        card_room = get_object_or_404(CardRoom, pk=pk)
        players = self.controller.get_players_names(card_room)

        # ROOM STATUS
        card_room_status = self.controller.get_room_status(card_room)
        print(card_room_status)

        register = self.controller.check_user(request.user, card_room)
        cancel = not register
        countdown = False
        if not card_room_status:
            print("the game will start")
            content = {
                'table_status': False,
                'game_status': True,
                'register': False,
                'cancel': False,
                'countdown': False,
                'timer': "0",
            }
            return render(request, self.template_name, content)

        content = {
            'players': players,
            'room_nr': pk,
            'register': register,
            'cancel': cancel,
            'countdown': countdown,
            'timer': "0",
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
