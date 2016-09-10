from django.db import models
from django.contrib.auth.models import AbstractUser

SAFETY_LEVELS = (
    (0, 'SAFE'),
    (1, 'UNREACHABLE'),
    (2, 'NEED_HELP')
)


class User(AbstractUser):
    """
    A custom User model.
    """
    pass


class Refugee(models.Model):
    """
    Used to store refugee information
    """

    user = models.OneToOneField(User)

    alternate_contact_number = models.CharField(max_length=20, blank=True)
    safety_level = models.IntegerField(choices=SAFETY_LEVELS)

