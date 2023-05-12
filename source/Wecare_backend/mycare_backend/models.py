from _decimal import Decimal
from datetime import datetime

from django.db import models


# Create your models here.


class TempInfo(models.Model):
    temperature = models.DecimalField(max_digits=6, decimal_places=2)
    update_time = models.DateTimeField() or datetime.now()


class HeartInfo(models.Model):
    heart_rate = models.DecimalField(max_digits=6, decimal_places=2)
    update_time = models.DateTimeField() or datetime.now()


class BodyStatusInfo(models.Model):
    body_status = models.CharField(max_length=10)
    update_time = models.DateTimeField() or datetime.now()

