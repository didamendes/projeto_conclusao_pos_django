from django.db import models

# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=100, blank=False, verbose_name='Nome')
    nacionalidade = models.CharField(max_length=100, blank=False, verbose_name='Nacionalidade')
    dataNascimento = models.DateField(blank=False, verbose_name='Data de Nascimento')

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
