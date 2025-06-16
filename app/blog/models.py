from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-fecha_creacion']
