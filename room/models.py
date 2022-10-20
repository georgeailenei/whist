from django.db import models
from userauth.models import User


class CardRoom(models.Model):
    players = models.ManyToManyField(User)
    started = models.BooleanField()


"""
CARDROOM

id
1     
2    
3    

"""


"""
Intermidiara
room_id  user_id
1 1
1 2
1 3
2 4
2

"""


"""
USER

id  username parola ......
1   Dan
2   Robert
3   Sandu
4   Nicu
5   Axinte
6   Leana


"""