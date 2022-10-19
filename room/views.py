from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .utils import get_controller


class CardRooms(TemplateView):
    template_name = 'room/CardRoom.html'

    def __init__(self):
        super().__init__()
        self.controller = get_controller()

    def post(self, request):
        if request.method == 'POST':
            if request.user.is_authenticated:
                user = request.user
                # SAVE THE PLAYER IN CardRoom DB
                self.controller.add_player(user)
                # YOU MUST IMPLEMENT USER VALIDATION
                # EXAMPLE: IF THE USER IS IN THE LIST; CANNOT JOIN AGAIN
            else:
                print("You must login to join the table")
        return redirect('CardRooms')

    def get(self, request):
        return render(request, self.template_name)
