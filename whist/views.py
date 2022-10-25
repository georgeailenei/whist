from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from whist.forms import GameForm
from whist.utils import get_controller


class GamesView(TemplateView):
    template_name = 'whist/games.html'


class WhistView(TemplateView):
    template_name = 'whist/whist.html'

    def __init__(self):
        super().__init__()
        self.controller = get_controller()

    def post(self, request):
        form = GameForm(request.POST)
        if form.is_valid():
            card = form.cleaned_data['input']
            if self.controller.card_validator.check_card(card):
                self.controller.save_card(card)
            form = GameForm()
            return redirect('whist')

    def get(self, request):
        # Card Receiver
        form = GameForm()

        # RUN GAME
        content = self.controller.run_game(form)
        return render(request, self.template_name, content)
