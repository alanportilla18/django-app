from django.contrib import admin
from .models import User, Identification_type, Countries, Deparments, Cities, Persons, Students

# Register your models here.
class UserFields(admin.ModelAdmin):
    list_display = [ 'email','password', 'status' ]

admin.site.register(User, UserFields)
admin.site.register(Identification_type)
admin.site.register(Countries)
admin.site.register(Deparments)
admin.site.register(Cities)
admin.site.register(Persons)
admin.site.register(Students)