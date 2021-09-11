from django.contrib import admin

from .models import Category, Post, Comment, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ist_display = ('pk', 'name', 'slug')


class CommentInline(admin.StackedInline):
    model = Comment
    extra = False


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('pk', 'title', 'updated_at', 'status')
    search_fields = ('tags', 'pk', 'created_at')
    list_filter = ('tags', 'status')
    inlines = (CommentInline,)

