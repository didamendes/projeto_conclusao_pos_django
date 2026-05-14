from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django_tables2 import SingleTableView

from .forms import AutorForm, CadastroForm
from .models import Autor, Usuario
from .tables import AutorTable


# Create your views here.
class AutorMenuView(LoginRequiredMixin, SingleTableView):
    model = Autor
    table_class = AutorTable
    template_name_suffix = "_menu"
    table_pagination = {"per_page": 5}
    template_name = 'autor/autor_menu.html'

class AutorCreateView(LoginRequiredMixin, CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'autor/autor_form.html'
    def get_success_url(self):
        return reverse_lazy('autor_menu')

class AutorUpdateView(LoginRequiredMixin, UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'autor/autor_form.html'

    def get_success_url(self):
        return reverse_lazy('autor_menu')

class AutorDeleteView(LoginRequiredMixin, DeleteView):
    model = Autor
    success_url = reverse_lazy('autor_menu')


class CadastroUsuarioView(CreateView):
    model = Usuario
    form_class = CadastroForm
    template_name = 'usuarios/cadastro.html'
    success_url = reverse_lazy('autor_menu')