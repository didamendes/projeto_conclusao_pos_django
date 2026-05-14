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

admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Livro)
admin.site.register(Emprestimo)
admin.site.register(Avaliacao)
