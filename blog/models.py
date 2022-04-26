from django.db import models

class Post(models.Model):

    title  = models.CharField(max_length=50)
    author = models.ForeignKey(
        'auth.user',
        on_delete=models.CASCADE,
    )
    body = models.TextField(max_length=500)

    def __str__(self) -> str:
        return self.title
