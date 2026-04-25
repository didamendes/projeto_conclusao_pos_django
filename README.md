<div align="center">

# 📚 Biblioteca — Sistema de Gerenciamento de Autores

![Django](https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

**Aplicação web para cadastro e gerenciamento de autores literários, desenvolvida com Django 6 e Bootstrap 5.**

---

[Funcionalidades](#-funcionalidades) •
[Tecnologias](#-tecnologias) •
[Instalação](#-instalação) •
[Uso](#-uso) •
[Arquitetura](#-arquitetura) •
[Testes](#-testes) •
[Contribuição](#-contribuição)

</div>

---

## ✨ Funcionalidades

| Funcionalidade | Descrição |
|---|---|
| 📋 **Listagem de Autores** | Tabela paginada e interativa com ordenação, powered by `django-tables2` |
| ➕ **Cadastro de Autores** | Formulário com validação automática para inclusão de novos autores |
| ✏️ **Edição de Autores** | Atualização de dados via formulário pré-preenchido |
| 🗑️ **Exclusão com Confirmação** | Modal de confirmação antes da exclusão, evitando remoções acidentais |
| 🔐 **Autenticação** | Controle de acesso com sistema de login nativo do Django |
| 🛡️ **Painel Administrativo** | Interface admin customizada com filtros, busca e cálculo de idade |
| 📱 **Design Responsivo** | Layout adaptável a diferentes dispositivos via Bootstrap 5 |

---

## 🛠️ Tecnologias

### Back-end
- **[Django 6.0](https://www.djangoproject.com/)** — Framework web Python de alto nível
- **[Python 3.x](https://www.python.org/)** — Linguagem de programação
- **[SQLite](https://www.sqlite.org/)** — Banco de dados relacional embarcado

### Front-end
- **[Bootstrap 5](https://getbootstrap.com/)** — Framework CSS para UI responsiva
- **[django-bootstrap5](https://django-bootstrap5.readthedocs.io/)** — Integração Django + Bootstrap

### Bibliotecas Auxiliares
- **[django-tables2](https://django-tables2.readthedocs.io/)** — Renderização de tabelas HTML com paginação e ordenação

---

## 📁 Arquitetura

```
Estudo/
├── estudo/                     # Configuração do projeto Django
│   ├── settings.py             # Configurações gerais (DB, apps, i18n)
│   ├── urls.py                 # Rotas raiz do projeto
│   ├── wsgi.py                 # Entry point WSGI
│   └── asgi.py                 # Entry point ASGI
│
├── biblioteca/                 # App principal — Gerenciamento de Autores
│   ├── models.py               # Modelo Autor (nome, nacionalidade, data nasc.)
│   ├── views.py                # Class-Based Views (CRUD completo)
│   ├── urls.py                 # Rotas da app (/autor_create, /autor_update, etc.)
│   ├── forms.py                # ModelForm para o modelo Autor
│   ├── tables.py               # Configuração de tabelas (django-tables2)
│   ├── admin.py                # Admin customizado com campo de idade calculada
│   ├── tests.py                # Testes unitários
│   └── templates/
│       ├── base.html           # Template base com navbar Bootstrap
│       └── autor/
│           ├── autor_menu.html # Listagem + modal de exclusão
│           └── autor_form.html # Formulário de criação/edição
│
├── manage.py                   # CLI do Django
├── db.sqlite3                  # Banco de dados SQLite
└── .gitignore                  # Regras de exclusão do Git
```

---

## 🚀 Instalação

### Pré-requisitos

- Python 3.10+ instalado
- `pip` (gerenciador de pacotes Python)
- Git

### Passo a passo

**1. Clone o repositório**

```bash
git clone https://github.com/seu-usuario/projeto-biblioteca.git
cd projeto-biblioteca
```

**2. Crie e ative o ambiente virtual**

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate
```

**3. Instale as dependências**

```bash
pip install django django-bootstrap5 django-tables2
```

**4. Execute as migrações**

```bash
python manage.py migrate
```

**5. Crie um superusuário (para acesso ao admin)**

```bash
python manage.py createsuperuser
```

**6. Inicie o servidor de desenvolvimento**

```bash
python manage.py runserver
```

**7. Acesse no navegador**

| Recurso | URL |
|---|---|
| Aplicação | [http://localhost:8000](http://localhost:8000) |
| Painel Admin | [http://localhost:8000/admin](http://localhost:8000/admin) |

---

## 💻 Uso

### Listagem de Autores

A página inicial exibe uma tabela paginada com todos os autores cadastrados. Cada registro possui botões de **Editar** e **Excluir**.

### Cadastro

Clique em **"Incluir novo autor"** para acessar o formulário de cadastro. Preencha os campos obrigatórios:

- **Nome** — Nome completo do autor
- **Nacionalidade** — País de origem
- **Data de Nascimento** — Formato dd/mm/aaaa

### Edição

Clique no nome do autor na tabela ou no botão **Editar** para modificar os dados.

### Exclusão

Clique em **Excluir** para abrir o modal de confirmação. Confirme a exclusão clicando em **"Sim, excluir"**.

### Painel Administrativo

Acesse `/admin` com as credenciais de superusuário para uma interface avançada com:

- 🔍 Busca por nome e nacionalidade
- 📊 Filtros por nacionalidade e data de nascimento
- 📅 Cálculo automático da idade aproximada do autor

---

## 🧪 Testes

O projeto inclui testes unitários para formulários e views.

```bash
# Executar todos os testes
python manage.py test

# Executar com verbosidade
python manage.py test -v 2

# Executar testes específicos
python manage.py test biblioteca.tests.AutorFormTest
python manage.py test biblioteca.tests.AutorViewTest
```

### Cobertura dos Testes

| Classe | Cenário |
|---|---|
| `AutorFormTest` | Verifica a inicialização do formulário e presença dos campos |
| `AutorViewTest` | Valida a view de criação (status code e template utilizado) |

---

## 🏗️ Padrões de Projeto

- **MVT (Model-View-Template)** — Arquitetura padrão do Django
- **Class-Based Views (CBVs)** — Views genéricas para operações CRUD (`CreateView`, `UpdateView`, `DeleteView`, `SingleTableView`)
- **Template Inheritance** — Template base (`base.html`) com blocos reutilizáveis
- **ModelForm** — Formulários gerados automaticamente a partir do modelo
- **DRY (Don't Repeat Yourself)** — Reutilização de templates e componentes

---

## 🔧 Configurações Relevantes

| Configuração | Valor |
|---|---|
| Idioma | `pt-br` (Português Brasileiro) |
| Banco de Dados | SQLite 3 |
| Paginação | 5 registros por página |
| Framework CSS | Bootstrap 5 |
| Debug | `True` (desenvolvimento) |

---

</div>
