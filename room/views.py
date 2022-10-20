from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView

from room.models import CardRoom
from .utils import get_controller
from django.contrib.auth.mixins import LoginRequiredMixin


class CardRooms(LoginRequiredMixin, TemplateView):
    template_name = 'room/CardRoom.html'

    def __init__(self):
        super().__init__()
        self.controller = get_controller()

    def post(self, request, pk):
        card_room = get_object_or_404(CardRoom, pk=pk)

        if request.method == 'POST':
            user = request.user
            # SAVE THE PLAYER IN CardRoom DB
            self.controller.add_player(user, card_room)
            # YOU MUST IMPLEMENT USER VALIDATION
            # EXAMPLE: IF THE USER IS IN THE LIST; CANNOT JOIN AGAIN
        
        return redirect('card_rooms', pk=pk)

    def get(self, request, pk):
        return render(request, self.template_name)
