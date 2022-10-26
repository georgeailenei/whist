from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager


class User(AbstractUser, PermissionsMixin):
    pass
