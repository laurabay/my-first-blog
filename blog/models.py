from django.db import models
from django.utils import timezone


class Post(models.Model):
        author = models.ForeignKey('auth.User')
        titulo = models.CharField(max_length=200)
        autor = models.CharField(max_length=200)
        genero = models.CharField(max_length=200)
        editorial = models.CharField(max_length=200)
        fecha_publicacion = models.CharField(max_length=200)
        imagen = models.ImageField(upload_to='photos/')
        sinopsis = models.TextField()
        created_date = models.DateTimeField(
                default=timezone.now)
        published_date = models.DateTimeField(
                blank=True, null=True)

        def publish(self):
            self.published_date = timezone.now()
            self.save()

        def __str__(self):
            return self.titulo

       
