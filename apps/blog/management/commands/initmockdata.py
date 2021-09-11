import random

import psycopg2
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from django_seed import Seed

from apps.blog.models import Category, Post, Comment, Tag


class Command(BaseCommand):
    """Команда для создания тестовых данных"""
    def handle(self, *args, **options):
        try:
            seeder = Seed.seeder()

            seeder.add_entity(Category, 10, {
                'slug': '',
            })
            seeder.add_entity(Tag, 10, {
                'slug': '',
            })
            seeder.add_entity(Post, 30, {
                'slug': '',
                'status': lambda x: random.choice(['draft', 'published'])
            })
            seeder.add_entity(Comment, 90, {
                'user': lambda x: User.objects.get(pk=random.randint(1, 5)),
                'active': lambda x: random.choice([True, False])
            })

            seeder.execute()

            # создаем записи в вспомогательной таблице связи многие ко многим между постами и категориями постов
            category_ids = list(Category.objects.values_list('pk', flat=True))
            post_ids = list(Post.objects.values_list('pk', flat=True))

            category_to_post = []
            for post_id in post_ids:
                random.shuffle(category_ids)
                post_categories = category_ids[:3]

                for category_id in post_categories:
                    post_category = Post.categories.through(category_id=category_id, post_id=post_id)
                    category_to_post.append(post_category)
            Post.categories.through.objects.bulk_create(category_to_post, batch_size=1000)

            # создаем записи в вспомогательной таблице связи многие ко многим между постами и тегами постов
            tag_ids = list(Tag.objects.values_list('pk', flat=True))

            tag_to_post = []
            for post_id in post_ids:
                random.shuffle(tag_ids)
                post_tags = tag_ids[:3]

                for tag_id in post_tags:
                    post_tag = Post.tags.through(tag_id=tag_id, post_id=post_id)
                    tag_to_post.append(post_tag)
            Post.tags.through.objects.bulk_create(tag_to_post, batch_size=1000)
        except (IntegrityError, psycopg2.Error) as e:
            print('Command error:\n'
                  f'{e}'
                  'Probably the command was used repeatedly - the command can only be executed 1 time')
