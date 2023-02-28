from room.models import Stats


class RoomStats:
    def get_room_stats(self, room):
        if hasattr(room, "stats") is False:
            return Stats.objects.create(room=room)
        else:
            return room.stats
