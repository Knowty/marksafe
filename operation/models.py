from django.db import models

# Create your models here.
class Operation(models.Model):
    """
    Used to store Operation information
    """

    name = models.CharField(max_length=64)
    comments = models.TextField(null=True)
    status = models.TextField()