from django.contrib import admin
from.models import Product, DigitalProduct



# Register your models here.
admin.site.register(Product)    #---> con eso ya va a estar disponible dentro del admin
admin.site.register(DigitalProduct)