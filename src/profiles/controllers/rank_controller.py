from userauth.models import User


def ranking(user):
    users = User.objects.all().order_by('points').values()
    position = 1

    for u in users:
        if user.username == u['username']:
            return position
        else:
            position += 1
