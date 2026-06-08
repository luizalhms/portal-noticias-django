# Portal de Notícias Django

## Descrição

O Portal de Notícias é uma aplicação web desenvolvida em Python utilizando o framework Django. O sistema permite o gerenciamento e publicação de notícias por meio do painel administrativo do Django, possibilitando o cadastro, edição e exclusão de conteúdos.

O projeto foi desenvolvido como atividade da disciplina de Programação Web, com o objetivo de aplicar conceitos de desenvolvimento web utilizando o padrão MVC/MVT, banco de dados relacional e controle de versão com Git e GitHub.

## Equipe

* Luiza Helena Melo Silva – GitHub: Beatriz862
* Giovana Lima Pequeno – GitHub: giovanalimapequeno

## Tecnologias Utilizadas

* Python 3.11.4
* Django 5.2.15
* SQLite3
* HTML5
* CSS3
* Git
* GitHub
* Visual Studio Code

## Funcionalidades Implementadas

### Escopo Base

* Cadastro de notícias
* Listagem de notícias
* Edição de notícias
* Exclusão de notícias
* Painel administrativo do Django
* Banco de dados para armazenamento das notícias
* Controle de usuários administradores

## Pré-requisitos

* Python 3.x
* pip
* virtualenv
* Git

## Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/Beatriz862/portal-noticias-django.git
```

### 2. Entrar na pasta do projeto

```bash
cd portal-noticias-django
```

### 3. Criar ambiente virtual

```bash
python -m venv venv
```

### 4. Ativar ambiente virtual

Windows:

```bash
venv\Scripts\activate
```

### 5. Instalar dependências

```bash
pip install django
```

### 6. Executar migrações

```bash
python manage.py migrate
```

### 7. Criar superusuário

```bash
python manage.py createsuperuser
```

### 8. Executar servidor

```bash
python manage.py runserver
```

### 9. Acessar sistema

Portal:

```text
http://127.0.0.1:8000/
```

Painel Administrativo:

```text
http://127.0.0.1:8000/admin/
```

## Usuário de Teste

Administrador:

* Usuário: admin
* Senha: 123
## Capturas de Tela

Adicionar imagens das principais telas do sistema:

<img width="1088" height="713" alt="Captura de tela 2026-06-07 201927" src="https://github.com/user-attachments/assets/5c8b0ae5-5146-413f-b164-8f069ed5e9ab" />
<img width="1061" height="702" alt="Captura de tela 2026-06-07 203430" src="https://github.com/user-attachments/assets/8ddca2c8-082f-47e2-bd65-0fc40f315e29" />
<img width="1061" height="714" alt="Captura de tela 2026-06-07 202428" src="https://github.com/user-attachments/assets/0c63ac57-2338-4dc3-a97a-ad8799ef6bf2" />

## Diagrama Entidade-Relacionamento:

<img width="648" height="452" alt="Captura de tela 2026-06-07 210414" src="https://github.com/user-attachments/assets/d8b0b295-7dbc-491e-89be-3a2646c10760" />




