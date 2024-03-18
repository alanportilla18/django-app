from django.contrib import admin
from .models import User, Identification_type, Countries, Deparments, Cities, Persons, Students

admin.site.register(User)
admin.site.register(Identification_type)
admin.site.register(Countries)
admin.site.register(Deparments)
admin.site.register(Cities)
admin.site.register(Persons)
admin.site.register(Students)