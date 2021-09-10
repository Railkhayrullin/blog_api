from django.db import models
from django.conf import settings


class Category(models.Model):
    """Категории статьи"""
    name = models.CharField('категория статьи', max_length=255, blank=False)
    slug = models.SlugField('slug', max_length=255, unique=True, blank=False)
    description = models.CharField('описание категории', max_length=1024, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория статьи'
        verbose_name_plural = 'категории статьи'


class Post(models.Model):
    """Модель статьи"""
    STATUS_CHOICES = (
        ('draft', 'Черновик'),
        ('published', 'Опубликовано'),
    )
    category = models.ManyToManyField(
        Category,
        verbose_name='категория статьи',
        related_name='category_posts',
        blank=False
    )
    tag = models.ManyToManyField(
        'Tags',
        verbose_name='тег статьи',
        related_name='tag_posts',
        blank=True,
        null=True
    )
    title = models.CharField('заголовок статьи', max_length=255, blank=False)
    slug = models.SlugField('slug', max_length=255, unique=True, blank=False)
    content = models.TextField('текст статьи', max_length=10000, blank=False)
    created_at = models.DateField('дата создания', auto_now=True)
    update_at = models.DateField('дата обновления', auto_now_add=True)
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'


class Comment(models.Model):
    """Модель комментария"""
    post = models.ForeignKey(Post, verbose_name='пост', related_name='post_comments', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='пользователь', on_delete=models.CASCADE)
    text = models.TextField('текст комментариия', max_length=255, blank=False)
    created_at = models.DateTimeField('дата создания', auto_now=True)
    active = models.BooleanField('активный', default=False)

    def __str__(self):
        return f'Комментарий от {self.user.first_name} к посту {self.post.title}'

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'


class Tags(models.Model):
    """Модель тегов для статей"""
    name = models.CharField('тег', max_length=64, blank=False)
    slug = models.SlugField('slug', max_length=64, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'
