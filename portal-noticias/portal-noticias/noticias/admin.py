from django.contrib import admin

from .models import Noticia, Tarefa


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'categoria', 'data_publicacao', 'visualizacoes')
    list_filter = ('categoria', 'data_publicacao', 'autor')
    search_fields = ('titulo', 'conteudo', 'categoria', 'autor__username')


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'concluida', 'data_criacao', 'data_conclusao')
    list_filter = ('concluida', 'data_criacao', 'autor')
    search_fields = ('titulo', 'descricao', 'autor__username')

