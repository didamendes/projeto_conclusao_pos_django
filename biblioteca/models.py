from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=100, blank=False, verbose_name='Nome')
    nacionalidade = models.CharField(max_length=100, blank=False, verbose_name='Nacionalidade')
    dataNascimento = models.DateField(blank=False, verbose_name='Data de Nascimento')

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']

class Usuario(AbstractUser):
    telefone = models.CharField(max_length=20, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.get_full_name() or self.username

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Livro(models.Model):
    GENERO = [
        ('ficcao', 'Ficção Científica'),
        ('fantasia', 'Fantasia'),
        ('terror', 'Terror'),
        ('romance', 'Romance'),
        ('misterio', 'Mistério'),
        ('biografia', 'Biografia'),
        ('historia', 'História'),
        ('tecnologia', 'Tecnologia'),
        ('autoajuda', 'Autoajuda'),
        ('outro', 'Outro'),
    ]

    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    sinopse = models.TextField()
    genero = models.CharField(max_length=25, choices=GENERO)
    ano_publicacao = models.IntegerField()
    quantidade_total = models.IntegerField(default=1)
    quantidade_disponivel = models.IntegerField(default=1)
    categorias = models.ManyToManyField(Categoria, related_name='livros', blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        ordering = ['titulo']

    def __str__(self):
        return f'{self.titulo} - {self.autor}'

    def esta_disponivel(self):
        return self.quantidade_disponivel > 0

class Emprestimo(models.Model):
    STATUS = [
        ('ativo', 'Ativo'),
        ('devolvido', 'Devolvido'),
        ('atrasado', 'Atrasado'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='emprestimos')
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='emprestimos')
    data_emprestimo = models.DateField(auto_now_add=True)
    data_prevista_devolucao = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='ativo')

    class Meta:
        verbose_name = 'Empréstimo'
        verbose_name_plural = 'Empréstimos'
        ordering = ['-data_emprestimo']

    def __str__(self):
        return f'{self.usuario} - {self.livro} - {self.status}'

class Avaliacao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='avaliacoes')
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='avaliacoes')
    nota = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comentario = models.TextField(null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        ordering = ['-criado_em']
        unique_together = ('usuario', 'livro')

    def __str__(self):
        return f'{self.usuario} avaliou {self.livro} com nota {self.nota}'