from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('noticia/<int:pk>/', views.noticia_detail, name='noticia_detail'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('painel/noticias/', views.admin_noticias, name='admin_noticias'),
    path('painel/noticias/criar/', views.noticia_create, name='noticia_create'),
    path('painel/noticias/<int:pk>/editar/', views.noticia_update, name='noticia_update'),
    path('painel/noticias/<int:pk>/excluir/', views.noticia_delete, name='noticia_delete'),
    path('painel/tarefas/', views.admin_tarefas, name='admin_tarefas'),
    path('painel/tarefas/criar/', views.tarefa_create, name='tarefa_create'),
    path('painel/tarefas/<int:pk>/editar/', views.tarefa_update, name='tarefa_update'),
    path('painel/tarefas/<int:pk>/excluir/', views.tarefa_delete, name='tarefa_delete'),
    path('sobre/', views.about, name='about'),
    path('contato/', views.contact, name='contact'),
]
