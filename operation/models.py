from django.db import models

# Create your models here.
class operation(models.Model):
    """
    Used to store refugee information
    """

    name = models.CharField(max_length=64)
    comments = models.TextField(null=True)
    status = models.TextField()