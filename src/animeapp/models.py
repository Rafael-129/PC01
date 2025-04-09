# animeapp/models.py

from django.db import models
from django.contrib.auth.models import User  # Si tienes un modelo de usuario personalizado, úsalo

class Anime(models.Model):
    title = models.CharField(max_length=255)
    synopsis = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return self.title

class AnimeFavorito(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('anime', 'user')  # Un usuario solo puede agregar un anime una vez

    def __str__(self):
        return f'{self.user.username} - {self.anime.title}'
