from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    """Команда для создания тестового суперпользователя"""
    def handle(self, *args, **options):
        users_list = [
            User(username=f'test_user_{i}',
                 email=f'test_user_{i}@gmail.com',
                 password=f'test_user_{i}')
            for i in range(1, 6)]
        User.objects.bulk_create(users_list)
        print('Test users accounts create.')
