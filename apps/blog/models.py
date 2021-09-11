from django.conf import settings
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    """Категории статьи"""
    name = models.CharField('категория статьи', max_length=64)
    slug = models.SlugField('slug', max_length=64, unique=True)
    description = models.CharField('описание категории', max_length=1024, blank=True, null=True)

    def get_posts_quantity(self):
        return self.category_posts.count()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория статьи'
        verbose_name_plural = 'категории статьи'

    def save(self, *args, **kwargs):
        if self.slug == '' or not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super(Category, self).save(*args, **kwargs)


class Post(models.Model):
    """Модель статьи"""
    STATUS_CHOICES = (
        ('draft', 'Черновик'),
        ('published', 'Опубликовано'),
    )
    categories = models.ManyToManyField(
        Category,
        verbose_name='категория статьи',
        related_name='category_posts',
    )
    tags = models.ManyToManyField(
        'Tag',
        verbose_name='тег статьи',
        related_name='tag_posts',
        blank=True
    )
    title = models.CharField('заголовок статьи', max_length=255)
    slug = models.SlugField('slug', max_length=255, unique=True)
    content = models.TextField('текст статьи', max_length=10000)
    created_at = models.DateField('дата создания', auto_now=True)
    updated_at = models.DateField('дата обновления', auto_now_add=True)
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='draft', verbose_name='статус')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.title, allow_unicode=True)
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    """Модель комментария"""
    post = models.ForeignKey(Post, verbose_name='пост', related_name='post_comments', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='пользователь', on_delete=models.CASCADE)
    text = models.TextField('текст комментариия', max_length=255, blank=False)
    created_at = models.DateTimeField('дата создания', auto_now=True)
    active = models.BooleanField('активный', default=False)

    def __str__(self):
        return f'Комментарий от {self.user} к посту {self.post.title}'

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'


class Tag(models.Model):
    """Модель тегов для статей"""
    name = models.CharField('тег', max_length=64)
    slug = models.SlugField('slug', max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'
