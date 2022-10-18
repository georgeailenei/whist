from django.shortcuts import render
from django.views.generic import TemplateView


class CardRooms(TemplateView):
    template_name = 'room/CardRoom.html'

    def post(self, request):
        pass

    # def get(self, request):
    #     pass
