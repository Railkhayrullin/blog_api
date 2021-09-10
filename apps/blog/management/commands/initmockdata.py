import random
from django_seed import Seed

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from apps.blog.models import Category, Post, Comment, Tag


class Command(BaseCommand):
    """Команда для создания тестовых данных"""
    def handle(self, *args, **options):
        seeder = Seed.seeder()
        seeder.add_entity(Category, 10, {
            'slug': '',
        })
        seeder.add_entity(Tag, 10, {
            'slug': '',
        })
        seeder.add_entity(Post, 30, {
            'slug': '',
            'status': 'published',
        })
        seeder.add_entity(Comment, 90, {
            'user': lambda x: User.objects.get(pk=random.randint(1, 5)),
            'active': True,
        })

        seeder.execute()
