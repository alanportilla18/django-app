from django.contrib import admin
from .models import Client, Product, Product_client, Transactions_type, Transactions

# Register your models here.
class UserFields(admin.ModelAdmin):
    list_display = [ ]

admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Product_client)
admin.site.register(Transactions_type)
admin.site.register(Transactions)