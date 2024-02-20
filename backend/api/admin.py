from django.contrib import admin

from .models import Car, Comment, Country, Producer

admin.site.register(Country)
admin.site.register(Producer)
admin.site.register(Car)
admin.site.register(Comment)
