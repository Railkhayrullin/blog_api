from rest_framework import serializers

from .models import Category, Post, Comment, Tag


class CategorySerializer(serializers.ModelSerializer):
    """Список категорий"""
    posts_count = serializers.CharField(source='get_posts_quantity')

    class Meta:
        model = Category
        fields = '__all__'


class CategoryCreateSerializer(serializers.ModelSerializer):
    """Сериалайзер для создания категории"""

    class Meta:
        model = Category
        exclude = ('slug',)


class PostCategorySerializer(serializers.ModelSerializer):
    """Список категорий для конкретного поста"""

    class Meta:
        model = Category
        fields = ('name',)


class TagSerializer(serializers.ModelSerializer):
    """Список тегов"""

    class Meta:
        model = Tag
        fields = '__all__'


class PostTagSerializer(serializers.ModelSerializer):
    """Список тегов для поста"""

    class Meta:
        model = Tag
        fields = ('name',)


class CommentSerializer(serializers.ModelSerializer):
    """Список комментариев"""

    class Meta:
        model = Comment
        fields = '__all__'


class CommentCreateSerializer(serializers.ModelSerializer):
    """Список комментариев"""

    class Meta:
        model = Comment
        exclude = ('active',)
        read_only_fields = ('user',)


class PostListSerializer(serializers.ModelSerializer):
    """Список постов"""
    tags = PostTagSerializer(read_only=True, many=True)
    categories = PostCategorySerializer(read_only=True, many=True)

    class Meta:
        model = Post
        exclude = ('content',)


class PostDetailSerializer(serializers.ModelSerializer):
    """Информация о посте с комментариями"""
    categories = PostCategorySerializer(read_only=True, many=True)
    tags = PostTagSerializer(read_only=True, many=True)
    post_comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'


class PostCreateSerializer(serializers.ModelSerializer):
    """Сериалайзер для создания поста"""

    class Meta:
        model = Post
        exclude = ('slug', )
