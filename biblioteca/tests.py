from django.test import TestCase
from django.urls import reverse
from .forms import autor_form

class AutorFormTest(TestCase):
    def test_form_initialization(self):
        form = autor_form()
        self.assertIn('nome', form.fields)
        self.assertIn('nacionalidade', form.fields)
        self.assertIn('dataNascimento', form.fields)

class AutorViewTest(TestCase):
    def test_autor_create_view_get(self):
        response = self.client.get(reverse('autor_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'autor/autor_form.html')
