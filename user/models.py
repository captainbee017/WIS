import re
from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    mid_name = models.CharField(max_length=100, blank=True)
    is_admin = models.BooleanField(default=False)

    @property
    def name(self):
        full_name = "{} {} {}".format(self.first_name.title(), self.mid_name.title(), self.last_name.title())
        full_name = re.sub(' +', ' ', full_name)
        return full_name

    def __str__(self):
        return self.email
