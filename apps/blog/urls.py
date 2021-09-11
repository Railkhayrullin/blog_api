from django.urls import path

from .views import PostViewSet, CategoryViewSet, CommentCreateViewSet

urlpatterns = [
    path('post/create/', PostViewSet.as_view({'post': 'create'})),
    path('post/', PostViewSet.as_view({'get': 'list'})),
    path('post/<str:slug>/', PostViewSet.as_view({'get': 'retrieve'})),
    path('category/create', CategoryViewSet.as_view({'post': 'create'})),
    path('category/', CategoryViewSet.as_view({'get': 'list'})),
    path('comment/create/', CommentCreateViewSet.as_view({'post': 'create'})),
]
