from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from django.db import models


def is_fullname(user_name):
    if not len(user_name.split(' ')) > 1:
        raise ValidationError('Error! Name should have first name and last name')

class User(models.Model):
    user_name = models.CharField(max_length=200, blank=False, unique=False, validators=[is_fullname])
    user_email = models.EmailField(max_length=254, blank=False, unique=False, validators=[validate_email])

    def __str__(self):
        return self.user_name + ", " + self.user_email
