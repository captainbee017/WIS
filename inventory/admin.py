from django.contrib import admin

# Register your models here.
from inventory.models import Item
from inventory.models import ItemCategory

admin.site.register(Item)
admin.site.register(ItemCategory)