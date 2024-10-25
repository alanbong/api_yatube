from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """Модель для групп."""
    title = models.CharField(
        max_length=100, verbose_name='Название группы')
    slug = models.SlugField(
        unique=True, max_length=100, verbose_name='Идентификатор группы')
    description = models.CharField(
        max_length=300, verbose_name='Описание группы')

    def __str__(self):
        return self.title


class Post(models.Model):
    """Модель для постов."""
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name='posts', null=True, blank=True)

    def __str__(self):
        return self.text


class Comment(models.Model):
    """Модель для комментариев к постам."""
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)


class Follow(models.Model):
    """Модель для подписок."""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('user', 'following'),
                name='unique_follow',
             ),

            models.CheckConstraint(
                check=models.Q(_negated=True, user=models.F('following')),
                name='user_cant_follow_himself',
            ),
        ]

    def __str__(self):
        return f'{self.user} подписан на {self.following}'
