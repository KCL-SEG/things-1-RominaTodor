from django.db import models
from django.core.validators import MaxValueValidator

class Thing(models.Model):
    # name must be unique, must not be blank, and must consist of 30 characters or less.
    name = models.CharField(max_length=30, unique=True, blank=False)
    # description need not be unique, may be blank, and must consist of 120 characters of less.
    description = models.TextField(max_length=120)
    # quantity need not be unique, and must be an integer value between 0 and 100 (inclusive). quantity may be 0 and it may be 100, but not less than 0 and not more than 100.
    quantity = models.PositiveIntegerField(validators=[MaxValueValidator(100)]
    )
