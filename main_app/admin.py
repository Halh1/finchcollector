from django.contrib import admin
from .models import Finch, Feeding, Birdhouse
# Register your models here.
admin.site.register([Finch, Feeding, Birdhouse])