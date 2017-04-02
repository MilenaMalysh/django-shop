from django.contrib import admin
from .models import AdditionalFunction, Instrument, Basket

admin.site.register(AdditionalFunction)
admin.site.register(Instrument)
admin.site.register(Basket)
