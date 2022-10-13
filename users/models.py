from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin


class CustomUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError("You haven't provide any email")
        email = self.normalize_email(email)
        username = self.model(email=email, **extra_fields)
        username.set_password(password)
        username.save(using=self._db)
        return username

    def create_user(self, username_field, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self.create_user(username_field, email, password, **extra_fields)

    def create_superuser(self, username_field, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username_field, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, blank=True, default='', unique=True)
    email = models.EmailField(blank=True, default='')

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField()
    last_login = models.DateTimeField(blank=True, null=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
