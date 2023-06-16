from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen_perfil = models.ImageField('Foto de perfil', upload_to='perfil', null=True, blank=True)

    def __str__(self):
        return f'{self.user.username}'
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
