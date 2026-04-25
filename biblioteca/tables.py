import django_tables2 as tables
from django_tables2.utils import A

from .models import Autor

class autor_table(tables.Table):
    nome = tables.LinkColumn("autor_update", args=[A("pk")])
    nacionalidade = tables.LinkColumn("autor_update", args=[A("pk")])
    dataNascimento = tables.LinkColumn("autor_update", args=[A("pk")])
    editar = tables.TemplateColumn(
        template_code='<a href="{% url \'autor_update\' record.pk %}" class="btn btn-primary btn-sm">Editar</a>',
        verbose_name="Editar"
    )
    excluir = tables.TemplateColumn(
        template_code='<button class="btn btn-danger btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" data-bs-id="{{ record.pk }}" data-bs-nome="{{ record.nome }}">Excluir</button>',
        verbose_name="Excluir"
    )
    class Meta:
        model = Autor
        attrs = {"class": "table thead-light table-striped table-hover"}
        template_name = "django_tables2/bootstrap4.html"
        fields = ("nome", "nacionalidade", "dataNascimento")