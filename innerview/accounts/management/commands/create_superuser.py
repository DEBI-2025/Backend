import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from dotenv import load_dotenv
load_dotenv()

class Command(BaseCommand):
    help = 'Create a superuser with additional fields if it doesn’t exist'

    def handle(self, *args, **kwargs):
        User = get_user_model()

        # Check if the superuser already exists
        if not User.objects.filter(email=os.getenv("super_user_email")).exists():
            User.objects.create_superuser(
                email=os.getenv("super_user_email"),
                first_name="DEBI",
                last_name="Team",
                phone="01022317563",
                date_of_birth="2000-1-1",
                password=os.getenv("super_user_pass")
            )
            self.stdout.write(self.style.SUCCESS('Successfully created superuser with additional fields'))
        else:
            self.stdout.write(self.style.SUCCESS('Superuser already exists'))
