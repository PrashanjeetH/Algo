from django.contrib import admin
from .models import Country, Person, City
# Register your models here.
admin.site.register(Country)
admin.site.register(Person)
admin.site.register(City)
