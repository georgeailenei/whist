from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=40, unique=True)
    data_of_birth = models.DateField(unique=True)
    email = models.EmailField()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = email
    REQUIRED_FIELDS = ['data_of_birth']

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class CustomUserManager(BaseUserManager):
    def create_user(self, username, date_of_birth, email, password=None, **other_fields):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            **other_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, date_of_birth, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_activate', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigner to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigner to is_superuser=True.')

        return self.create_user(username, date_of_birth, email, password)
