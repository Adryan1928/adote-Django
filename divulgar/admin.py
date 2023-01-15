from django.contrib import admin
from .models import Raca, tag, Pet
# Register your models here.
admin.site.register(Raca)
admin.site.register(tag)
admin.site.register(Pet)