from django.db import models
from django.core.validators import RegexValidator

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be in format: +60000000")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=False)

    def __str__(self):
        return self.name
