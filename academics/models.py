import datetime
from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length =250)
    status = models.BooleanField(default = True)
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null =True, blank = True)

class Students(models.Model):
    code = models.CharField(max_length = 50)
    id_person = models.IntegerField()
    status = models.BooleanField(default = True)
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null =True, blank = True)

class Identifications_type(models.Model):
    name = models.CharField(max_length = 50)
    abrev = models.CharField(max_length = 10)
    descrip = models.CharField(max_length = 100)
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null =True, blank = True)

class Persons(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    id_ident_type = models.IntegerField()
    ident_number = models.CharField(max_length =15)
    id_exp_city = models.IntegerField()
    address = models.CharField(max_length =150)
    mobile = models.CharField(max_length =50)
    id_user = models.IntegerField()
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null =True, blank = True)

class Cities(models.Model):
    name = models.CharField(max_length = 100)
    abrev = models.CharField(max_length =10)
    descrip = models.CharField(max_length =10)
    id_dept = models.IntegerField()
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null =True, blank = True)

class Deparments(models.Model):
    name = models.CharField(max_length = 100)
    abrev = models.CharField(max_length =10)
    descrip = models.CharField(max_length =10)
    id_country = models.IntegerField()
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null =True, blank = True)

class Countries(models.Model):
    name = models.CharField(max_length = 100)
    abrev = models.CharField(max_length =10)
    descrip = models.CharField(max_length =10)
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null =True, blank = True)