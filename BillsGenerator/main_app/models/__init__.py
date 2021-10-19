# django
from django.db import models
from django.utils import timezone

class Products(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)

class Bills(models.Model):
    # User
    total = models.FloatField(null=False, blank=False)
    create_at = models.DateTimeField(auto_now_add=True, blank=True, editable=False)