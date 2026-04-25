from django import forms

from biblioteca.models import Autor


class autor_form(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'nacionalidade', 'dataNascimento']