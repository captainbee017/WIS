from django.db import models

# Create your models here.
from common.models import Location, PhoneNumber
from user.models import User


class Customer(models.Model):
    user = models.OneToOneField(User)
    address = models.ForeignKey(Location, null=True, blank=True, related_name='customer')


class CustomerPhoneNumber(PhoneNumber):
    customer = models.ForeignKey(Customer, related_name='contact')

    def __str__(self):
        return self.customer.user.name