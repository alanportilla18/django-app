import datetime
from django.db import models

# Create your models here.

class dateTimeModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null = False, blank = False)
    updated_at = models.DateTimeField(auto_now=True, null = False, blank = False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    
    
    class Meta:
        abstract = True

class User(models.Model):
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length =250)
    status = models.BooleanField(default = True)

    def __str__(self):
        return " Correo: " +self.email +" Contraseña: " +self.password + " Estado: " + str(self.status)

class Students(models.Model):
    code = models.CharField(max_length = 50)
    id_person = models.ForeignKey('Persons', on_delete=models.CASCADE, blank=False)
    status = models.BooleanField(default = True)

    def __str__(self):
        return " Codigo: " +self.code +" ID: " +self.id_person + " Estado: " + str(self.status)

class Identification_type(models.Model):
    name = models.CharField(max_length = 50)
    abrev = models.CharField(max_length = 10)
    descrip = models.CharField(max_length = 100)
    
    def __str__(self):
        return " Nombre: " +self.name +" Abreviacion: " +self.abrev + " Descripcion: " + self.descrip

class Cities(models.Model):
    name = models.CharField(max_length = 100)
    abrev = models.CharField(max_length =10)
    descrip = models.CharField(max_length =10)
    id_dept = models.ForeignKey('Deparments', on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return " Nombre: " +self.name +" Abreviacion: " +self.abrev + " Descricion: " + self.descrip

class Persons(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    id_ident_type = models.ForeignKey('Identification_type', on_delete=models.CASCADE, blank=False)
    ident_number = models.CharField(max_length =15)
    id_exp_city = models.ForeignKey('Cities', on_delete=models.CASCADE, blank=False)
    address = models.CharField(max_length =150)
    mobile = models.CharField(max_length =50)
    id_user = models.ForeignKey('User', on_delete=models.CASCADE, blank=False)
    def __str__(self):
        return " Nombres: " +self.first_name +" Apellidos: " +self.last_name + " #Identificacion: " + self.ident_number + " Direccion: " +self.address + " Telefono: " +self.mobile

class Deparments(models.Model):
    name = models.CharField(max_length = 100)
    abrev = models.CharField(max_length =10)
    descrip = models.CharField(max_length =10)
    id_country = models.ForeignKey('Countries', on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return " Nombre: " +self.name +" Abreviacion: " +self.abrev + " Descripcion: " + self.descrip

class Countries(models.Model):
    name = models.CharField(max_length = 100)
    abrev = models.CharField(max_length =10)
    descrip = models.CharField(max_length =10)
    def __str__(self):
        return " Nombre: " +self.name +" Abreviacion: " +self.abrev + " Descripcion: " + self.descrip