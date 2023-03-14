from django.core.management.base import BaseCommand
from room.utils import game_controller, get_controller
from room.models import CardRoom
from userauth.models import User
from room.entities import Deck
from room.repos.room_stats import RoomStats

controller = get_controller()
game = game_controller()
room_stats = RoomStats()


class Command(BaseCommand):
    def handle(self, *args, **options):
        user1 = User.objects.create_superuser(username='admin')
        user1.set_password('admin')
        user1.save()
        user2 = User.objects.create(username='admin2')
        user2.set_password('admin')
        user2.save()
        user3 = User.objects.create(username='admin3')
        user3.set_password('admin')
        user3.save()
        user4 = User.objects.create(username='admin4')
        user4.set_password('admin')
        user4.save()

        card_room = CardRoom.objects.create()
        controller.add_player(user1, card_room)
        controller.add_player(user2, card_room)
        controller.add_player(user3, card_room)
        controller.add_player(user4, card_room)
        game.setup_room(card_room, Deck().cards)

        card_room_stats = room_stats.get_room_stats(card_room)
        card_room_stats.team_one_score = 4
        card_room_stats.team_two_score = 4
        card_room_stats.save()
