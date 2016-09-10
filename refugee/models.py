from django.db import models


SAFETY_LEVELS = (
    (0, 'SAFE'),
    (1, 'UNREACHABLE'),
    (2, 'NEED_HELP')
)


class Refugee(models.Model):
    """
    Used to store refugee information
    """

    name = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=20)
    photo = models.ImageField(blank=True, upload_to='refugee_photos')
    alternate_contact_number = models.CharField(max_length=20, blank=True)
    safety_level = models.IntegerField(choices=SAFETY_LEVELS)
    location = models.TextField()
