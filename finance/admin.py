from django.contrib import admin
from .models import Client, Product, Client_Product, TransactionType, Transaction

# Register your models here.
class UserFields(admin.ModelAdmin):
    list_display = [ ]

admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Client_Product)
admin.site.register(TransactionType)
admin.site.register(Transaction)