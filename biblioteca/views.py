from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django_tables2 import SingleTableView

from .forms import autor_form, CadastroForm
from .models import Autor, Usuario
from .tables import autor_table


# Create your views here.
class autor_menu(SingleTableView):
    model = Autor
    table_class = autor_table
    template_name_suffix = "_menu"
    table_pagination = {"per_page": 5}
    template_name = 'autor/autor_menu.html'

class autor_create(CreateView):
    model = Autor
    form_class = autor_form
    template_name = 'autor/autor_form.html'
    def get_success_url(self):
        return reverse_lazy('autor_menu')

class autor_update(UpdateView):
    model = Autor
    form_class = autor_form
    template_name = 'autor/autor_form.html'

    def get_success_url(self):
        return reverse_lazy('autor_menu')

class autor_delete(DeleteView):
    model = Autor
    success_url = reverse_lazy('autor_menu')


class cadastro_usuario(CreateView):
    model = Usuario
    form_class = CadastroForm
    template_name = 'usuarios/cadastro.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        usuario = form.save(commit=False)
        usuario.set_password(form.cleaned_data['password1'])
        usuario.save()

        grupo = form.cleaned_data['grupo']
        usuario.groups.add(grupo)

        return super().form_valid(form)