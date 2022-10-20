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

        if request.method == 'POST':
            user = request.user
            try:
                self.controller.add_player(user, card_room)
            except ValueError as p:
                return render(request, self.template_name, {'error': p})
        return redirect('card_rooms', pk=pk)

    def get(self, request, pk):
        card_room = get_object_or_404(CardRoom, pk=pk)
        players_waiting = self.controller.numbers_of_players_waiting(card_room)
        content = {
            'players': players_waiting,
        }
        return render(request, self.template_name, content)


class CardRooms(LoginRequiredMixin, ListView):
    model = CardRoom
    context_object_name = 'rooms'
