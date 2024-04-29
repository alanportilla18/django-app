from django import forms
from academics.models import User

class UserForm (forms.ModelForm):
    class Meta:
        Model = User 
        filed = [
            'emial',
            'password',
            'status'
        ]