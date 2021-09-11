from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Команда для создания тестового суперпользователя"""
    def handle(self, *args, **options):
        if User.objects.get(username="test_admin"):
            print('This admin account exist.')
        else:
            User.objects.create_superuser(username="test_admin", email="test_admin@gmail.com", password="test_admin")
            print('Test admin account create with:\n'
                  'username="test_admin"\n'
                  'password="test_admin"')
