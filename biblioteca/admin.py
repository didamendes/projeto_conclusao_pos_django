from django.contrib import admin
from .models import Autor, Usuario, Categoria, Livro, Emprestimo, Avaliacao
from datetime import date


# Register your models here.

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nacionalidade', 'dataNascimento', 'idade_atual')
    search_fields = ('nome', 'nacionalidade')
    list_filter = ('nacionalidade', 'dataNascimento')

    @admin.display(description='Idade Aproximada')
    def idade_atual(self, obj):
        if obj.dataNascimento:
            hoje = date.today()
            return hoje.year - obj.dataNascimento.year - (
                (hoje.month, hoje.day) < (obj.dataNascimento.month, obj.dataNascimento.day)
            )
        return "N/A"

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'telefone', 'is_active')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('is_active', 'groups')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'genero', 'ano_publicacao', 'quantidade_total', 'quantidade_disponivel')
    search_fields = ('titulo', 'autor')
    list_filter = ('genero', 'ano_publicacao')

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'livro', 'data_emprestimo', 'data_prevista_devolucao', 'status')
    search_fields = ('usuario__username', 'livro__titulo')
    list_filter = ('status', 'data_emprestimo')

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'livro', 'nota', 'criado_em')
    search_fields = ('usuario__username', 'livro__titulo')
    list_filter = ('nota', 'criado_em')
