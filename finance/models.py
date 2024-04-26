import datetime
from django.db import models

# Create your models here.

class dateTimeModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null = False, blank = False)
    updated_at = models.DateTimeField(auto_now=True, null = False, blank = False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    
    
    class Meta:
        abstract = True

class Client(models.Model):
    name = models.CharField(max_length = 80)
    last_name = models.CharField(max_length =80)
    email = models.CharField(max_length =100)
    phone = models.CharField(max_length =10)

    def __str__(self):
        return " Nombres: " +self.name +" Apellidos: " +self.last_name + " Correo: " + self.email + " Telefono: " + self.phone

class Product(models.Model):
    product_name = models.CharField(max_length = 50)
    abrev = models.CharField(max_length = 5)
    description = models.CharField(max_length = 500)

    def __str__(self):
        return " Nombre: " +self.product_name +" abreviatura: " +self.abrev + " descripcion: " + self.description

class Product_client(models.Model):
    id_client = models.ForeignKey('Client', on_delete=models.CASCADE, blank=False)
    id_product = models.ForeignKey('Product', on_delete=models.CASCADE, blank=False)
    number_count = models.CharField(max_length = 10)
    
    def __str__(self):
        return " ID Cliente: " +self.id_client +" ID Producto: " +self.id_product + " Numero de cuenta: " + self.number_count

class Transactions_type(models.Model):
    name = models.CharField(max_length = 20)
    abrev = models.CharField(max_length =5)
    descrip = models.CharField(max_length =200)

    def __str__(self):
        return " Nombre: " +self.name +" Abreviacion: " +self.abrev + " Descricion: " + self.descrip

class Transactions(models.Model):
    id_product_client = models.ForeignKey('Product_client', on_delete=models.CASCADE, blank=False)
    cost = models.IntegerField
    id_transactions_type = models.ForeignKey('Transactions_type', on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return " Prodcuto del cliente: " +self.id_product_client +" Costo: " +self.cost + " Tipo de transaccion: " + self.id_transactions_type
