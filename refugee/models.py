from django.db import models
from operation.models import Operation
SAFETY_LEVELS = (
    (0, 'SAFE'),
    (1, 'NOT CONFIRMED'),
    (2, 'UNREACHABLE'),
    (3, 'NEED_HELP'),
    (4, 'NOT IN ZONE')
)


class Refugee(models.Model):
    """
    Used to store refugee information
    """

    name = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=20)
    photo = models.ImageField(blank=True, upload_to='refugee_photos')
    alternate_contact_number = models.CharField(max_length=20, blank=True)
    safety_level = models.IntegerField(choices=SAFETY_LEVELS, default=1)
    retry_count = models.IntegerField(default=0)
    location = models.TextField(null=True)
    comments = models.TextField(null=True)
    status_updated_by = models.TextField(null=True)
    operation = models.ForeignKey(Operation,blank=True,default=None)
