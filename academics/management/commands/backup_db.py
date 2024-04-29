from django.core.management.base import BaseCommand
from academics.models import User
import json

class Command(BaseCommand):
    help = 'Make a database backup in JSON format'

    def handle(self, *args, **options):
        users = User.objects.all()

        data = [
            {
                'id':       user.id,
                'email':    user.email,
                'password': user.password,
                'status':   user.status
            }
            for user in users
        ]

        with open('backup_db.json','w') as file:
            json.dump(data, file, indent=4)