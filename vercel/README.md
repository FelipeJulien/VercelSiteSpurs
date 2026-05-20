# San Antonio Spurs - Site Informativo

![Django](https://img.shields.io/badge/Django-6.0-green)
![Tailwind CSS](https://img.shields.io/badge/Tailwind-CSS-blue)
![Python](https://img.shields.io/badge/Python-3.12-yellow)

## 📋 Descrição do Projeto

Este é um projeto acadêmico desenvolvido para a disciplina de **Programação Web** da Universidade Methodist University. O site é uma Multi-Page Application (MPA) dedicada à equipe de basquete profissional **San Antonio Spurs**, membro da NBA (National Basketball Association).

O projeto demonstra habilidades em desenvolvimento web usando:
- **Framework Django** para back-end e renderização server-side (SSR)
- **Template Engine nativo do Django** para construção de páginas
- **Tailwind CSS** via CDN para estilização responsiva e moderna
- **HTML5 semântico** para uma estrutura de documento acessível e bem organizada

---

## 🎯 Estrutura do Projeto

```
BasqueteSite/
├── core/                      # Aplicação principal Django
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── urls.py               # URLs do app core
│   ├── views.py              # Views do app core
│   └── ...
├── spurs_site/                # Configuração do projeto
│   ├── __init__.py
│   ├── settings.py           # Configurações do Django
│   ├── urls.py               # URL principal do projeto
│   ├── wsgi.py
│   └── asgi.py
├── static/                    # Arquivos estáticos
│   ├── css/
│   │   └── styles.css        # Estilos CSS customizados
│   ├── js/
│   └── images/
├── templates/                 # Templates HTML
│   ├── base.html              # Template base
│   ├── components/
│   │   ├── header.html       # Componente de navegação
│   │   └── footer.html       # Componente de rodapé
│   └── core/
│       ├── home.html         # Página inicial
│       ├── roster.html       # Página do elenco
│       ├── history.html      # Página da história
│       └── arena.html        # Página da arena
├── templates/
├── manage.py
└── README.md
```

---

## 🌐 Rotas e Views

O projeto implementa as seguintes rotas:

| URL | View | Descrição |
|-----|------|-----------|
| `/` | `home` | Página inicial com destaque para o time |
| `/roster/` | `roster` | Elenco atual com jogadores e comissão técnica |
| `/history/` | `history` | História do time com linha do tempo interativa |
| `/arena/` | `arena` | Informações sobre o Frost Bank Center |

### Configuração de URLs

**`core/urls.py`**:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('roster/', views.roster, name='roster'),
    path('history/', views.history, name='history'),
    path('arena/', views.arena, name='arena'),
]
```

**`spurs_site/urls.py`**:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
```

---

## 🎨 Abordagem CSS - Tailwind CSS

O projeto utiliza **Tailwind CSS via CDN** para estilização, o que oferece:

### Vantagens do Tailwind CSS

1. **Desenvolvimento Rápido**: Classes utilitárias permitem criar designs complexos sem escrever CSS customizado
2. **Responsividade**: Classes como `md:`, `lg:` facilitam criar layouts adaptativos
3. **Consistência**: Sistema de design integrado garante uniformidade visual
4. **Manutenção**: Sem necessidade de gerenciar arquivos CSS grandes

### Paleta de Cores Customizada

O projeto define cores personalizadas do Spurs:

```javascript
tailwind.config = {
    theme: {
        extend: {
            colors: {
                spurs: {
                    silver: '#B6B6B4',  // Prata característico
                    black: '#000000',   // Preto
                    navy: '#06143B',    // Azul marinho escuro
                    gray: '#63717A',    // Cinza
                }
            }
        }
    }
}
```

### CSS Customizado

Adicionalmente, `static/css/styles.css` contém personalizações extras:
- Gradientes de fundo
- Animações (float effect para o logo)
- Efeitos hover em cards

---

## 🏗️ Tags Semânticas HTML5

O projeto utiliza corretamente as tags semânticas do HTML5, cada uma com propósito específico:

### Estrutura Principal

```html
<body>
    <header>      <!-- Cabeçalho com navegação principal -->
    <main>       <!-- Conteúdo principal da página -->
    <footer>     <!-- Rodapé com informações extras -->
</body>
```

### Por Que Usar Tags Semânticas?

| Tag | Propósito | Benefício |
|-----|-----------|-----------|
| `<header>` | Define o cabeçalho da página | Indica claramente o início do conteúdo, melhora SEO |
| `<nav>` | Agrupa links de navegação | Facilita navegação por assistive technologies |
| `<main>` | Conteúdo principal único | Screen readers pulam navegação/rodapé |
| `<article>` | Conteúdo independente | Cartões de jogadores, cards de informação |
| `<section>` | Seção temática | Agrupa conteúdo relacionado logicamente |
| `<footer>` | Rodapé da página | Indica fim do documento, informações complementares |

### Exemplo de Estrutura Semântica

```html
<header>
    <nav>
        <ul>
            <li><a href="/">Início</a></li>
            <li><a href="/roster/">Elenco</a></li>
        </ul>
    </nav>
</header>

<main>
    <section>
        <h1>Título da Seção</h1>
        <article>Card de jogador 1</article>
        <article>Card de jogador 2</article>
    </section>
</main>

<footer>
    <p>© 2026 San Antonio Spurs Fan Site</p>
</footer>
```

---

## 🧩 Componentes Reutilizáveis

### Template Base (`base.html`)

O template base define a estrutura comum a todas as páginas:
- Importação do Tailwind CSS
- Configuração de cores customizadas
- Inclusão do header e footer
- Blocos `{% block %}` para conteúdo dinâmico

### Componente Header (`components/header.html`)

**Funcionalidades**:
- Logo clicável que retorna à página inicial
- Menu de navegação responsivo (mobile toggle)
- Indicação visual da página ativa usando `{% if request.path == '/' %}`
- Interação JavaScript para menu mobile

**Por que separar?**:
- Manutenção facilitada (alterar em um lugar reflete em todas)
- Princípio DRY (Don't Repeat Yourself)
- Componentização para projetos maiores

### Componente Footer (`components/footer.html`)

**Funcionalidades**:
- Links rápidos para todas as páginas
- Informações sobre o projeto acadêmico
- Tecnologias utilizadas (badges visuais)

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

- Python 3.10 ou superior
- pip (gerenciador de pacotes Python)

### Passo a Passo

1. **Clone ou baixe o projeto**

2. **Crie um ambiente virtual (recomendado)**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Instale as dependências**
```bash
pip install django
```

4. **Execute o servidor de desenvolvimento**
```bash
python manage.py runserver
```

5. **Acesse no navegador**
```
http://127.0.0.1:8000/
```

### Comandos Úteis do Django

```bash
# Criar migrations
python manage.py makemigrations

# Aplicar migrations
python manage.py migrate

# Criar superusuário (para admin)
python manage.py createsuperuser

# Iniciar servidor
python manage.py runserver

# Coleção de comandos disponíveis
python manage.py
```

---

## 📚 Tecnologias Utilizadas

| Tecnologia | Versão | Propósito |
|------------|--------|-----------|
| Django | 6.0 | Framework web backend |
| Python | 3.12 | Linguagem de programação |
| Tailwind CSS | Latest (CDN) | Framework CSS utilitário |
| HTML5 | - | Linguagem de marcação semântica |

---

## 🎓 Proposta Acadêmica

Este projeto foi desenvolvido como parte da avaliação da disciplina de **Programação Web** com os seguintes objetivos:

1. ✅ Demonstrar conhecimento em frameworks web (Django)
2. ✅ Implementar arquitetura MPA com SSR
3. ✅ Utilizar templates engine para componentização
4. ✅ Aplicar CSS moderno e responsivo
5. ✅ Estruturar HTML com tags semânticas apropriadas
6. ✅ Criar navegação funcional entre páginas

---

## 📝 Notas de Desenvolvimento

- O projeto utiliza **Tailwind CSS via CDN** para simplicidade em ambiente acadêmico
- As imagens dos jogadores são links externos da NBA (podem expirar)
- O projeto não inclui backend de banco de dados (estático para esta entrega)
- Todas as páginas são Server-Side Rendered pelo Django

---

## 👥 Autores

Projeto desenvolvido para fins acadêmicos.

**Disciplina**: Programação Web  
**Instituição**: Methodist University

---

## 📄 Licença

Este é um projeto acadêmico. O conteúdo relacionado ao San Antonio Spurs e NBA são marcas registradas de suas respectivas organizações.

---

*Go Spurs Go!* 🏀
