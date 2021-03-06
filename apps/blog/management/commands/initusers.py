from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Команда для создания тестового суперпользователя"""
    def handle(self, *args, **options):
        if User.objects.get(username='test_user_1'):
            print('This user accounts exist.')
        else:
            users_list = [
                User(username=f'test_user_{i}',
                     email=f'test_user_{i}@gmail.com',
                     password=f'test_user_{i}')
                for i in range(1, 6)]
            User.objects.bulk_create(users_list)
            print('Test user accounts create.')
