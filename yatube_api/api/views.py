from django.shortcuts import get_object_or_404
from rest_framework import filters, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from posts.models import Group, Post
from .viewsets import BaseListCreateViewSet
from .permissions import IsOwnerOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class PostViewSet(viewsets.ModelViewSet):
    """ViewSet для управления постами.

    Поддерживает:
    - Методы: list, retrieve — для всех пользователей.
    - Методы: create — для аутентифицированных пользователей.
    - Методы: update, partial_update, destroy — только для авторов постов.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """Установка автором поста текущего пользователя."""
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для получения информации о группах.

    Поддерживает:
    - Методы: list, retrieve — доступны всем пользователям.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.AllowAny]


class FollowViewSet(BaseListCreateViewSet):
    """ViewSet для управления подписками.

    Поддерживает:
    - Методы: list, create — для аутентифицированных пользователей.
    """
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['following__username']

    def get_queryset(self):
        """Возвращает подписки текущего пользователя."""
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        """Создаёт подписку."""
        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet для управления комментариями.

    Поддерживает:
    - Методы: list, retrieve — для всех пользователей.
    - Методы: create — для аутентифицированных пользователей.
    - Методы: update, partial_update, destroy — только для авторов комментов.
    """
    serializer_class = CommentSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_post(self):
        """Возвращает объект поста по его id."""
        return get_object_or_404(Post, id=self.kwargs['post_id'])

    def get_queryset(self):
        """Возвращает комментарии поста."""
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        """Устанавливает автором комментария текущего пользователя."""
        serializer.save(author=self.request.user, post=self.get_post())
