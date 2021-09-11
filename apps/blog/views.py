from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated

from .filters import PostFilter
from .models import Post, Category
from .serializers import PostListSerializer, \
    PostDetailSerializer, \
    PostCreateSerializer, \
    CategorySerializer, \
    CategoryCreateSerializer, \
    CommentCreateSerializer
from .service import PaginationPosts


class PostViewSet(viewsets.ModelViewSet):
    """Вывод списка статей/конкретной статьи с комментариями/создание статьи"""
    pagination_class = PaginationPosts
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filter_class = PostFilter
    ordering_fields = ['created_at', 'tags']
    search_fields = ['title', 'categories__name']

    def get_queryset(self):
        if self.action == 'list':
            posts = Post.objects.filter(status='published').prefetch_related('tags', 'categories')
        elif self.action == 'retrieve':
            posts = Post.objects.all()
        else:
            posts = Post.objects \
                .filter(status='published', post_comments__active=True) \
                .prefetch_related('post_comments__user')
        return posts

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        elif self.action == 'retrieve':
            return PostDetailSerializer
        else:
            return PostCreateSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """Вывод списка категорий/создание категории"""

    def get_queryset(self):
        if self.action == 'list':
            category = Category.objects.all()
        else:
            category = Category.objects.all()
        return category

    def get_serializer_class(self):
        if self.action == 'list':
            return CategorySerializer
        else:
            return CategoryCreateSerializer


class CommentCreateViewSet(viewsets.ModelViewSet):
    """Добавление комментария"""
    serializer_class = CommentCreateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
