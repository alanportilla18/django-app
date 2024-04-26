from django.contrib import admin
from .models import Client, Product, Client_product, Transaction_type, Transaction

# Register your models here.
class UserFields(admin.ModelAdmin):
    list_display = [ ]

admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Client_product)
admin.site.register(Transaction_type)
admin.site.register(Transaction)