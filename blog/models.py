from django.db import models

class Post(models.Model):

    title  = models.CharField(max_length=50, verbose_name='Заголовок статьи')
    author = models.ForeignKey(
        'auth.user',
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    body = models.TextField(max_length=500, verbose_name='Текст')

    def __str__(self) -> str:
        return self.title
