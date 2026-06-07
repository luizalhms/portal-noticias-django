from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import F, Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import NoticiaForm, RegisterForm, TarefaForm
from .models import Noticia, Tarefa


def home(request):
    query = request.GET.get('q', '')
    noticias = Noticia.objects.all()
    if query:
        noticias = noticias.filter(
            Q(titulo__icontains=query)
            | Q(conteudo__icontains=query)
            | Q(categoria__icontains=query)
            | Q(autor__username__icontains=query)
        )
    context = {
        'noticias': noticias,
        'query': query,
    }
    return render(request, 'noticias/home.html', context)


def noticia_detail(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    Noticia.objects.filter(pk=pk).update(visualizacoes=F('visualizacoes') + 1)
    noticia.refresh_from_db()
    return render(request, 'noticias/noticia_detail.html', {'noticia': noticia})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso.')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'noticias/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login realizado com sucesso.')
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'noticias/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'Você foi desconectado.')
    return redirect('home')


@login_required
def admin_noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticias/noticia_list.html', {'noticias': noticias})


@login_required
def noticia_create(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.autor = request.user
            noticia.save()
            messages.success(request, 'Notícia criada com sucesso.')
            return redirect('admin_noticias')
    else:
        form = NoticiaForm()
    return render(request, 'noticias/noticia_form.html', {'form': form, 'title': 'Criar notícia'})


@login_required
def noticia_update(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Notícia atualizada com sucesso.')
            return redirect('admin_noticias')
    else:
        form = NoticiaForm(instance=noticia)
    return render(request, 'noticias/noticia_form.html', {'form': form, 'title': 'Editar notícia'})


@login_required
def noticia_delete(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    if request.method == 'POST':
        noticia.delete()
        messages.success(request, 'Notícia excluída com sucesso.')
        return redirect('admin_noticias')
    return render(request, 'noticias/noticia_confirm_delete.html', {'noticia': noticia})


@login_required
def admin_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'noticias/tarefa_list.html', {'tarefas': tarefas})


@login_required
def tarefa_create(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.autor = request.user
            if tarefa.concluida and tarefa.data_conclusao is None:
                tarefa.data_conclusao = timezone.now()
            tarefa.save()
            messages.success(request, 'Tarefa criada com sucesso.')
            return redirect('admin_tarefas')
    else:
        form = TarefaForm()
    return render(request, 'noticias/tarefa_form.html', {
        'form': form,
        'title': 'Criar tarefa',
        'tarefa': None,
    })


@login_required
def tarefa_update(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            tarefa = form.save(commit=False)
            if tarefa.concluida and tarefa.data_conclusao is None:
                tarefa.data_conclusao = timezone.now()
            elif not tarefa.concluida:
                tarefa.data_conclusao = None
            tarefa.save()
            messages.success(request, 'Tarefa atualizada com sucesso.')
            return redirect('admin_tarefas')
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'noticias/tarefa_form.html', {
        'form': form,
        'title': 'Editar tarefa',
        'tarefa': tarefa,
    })


@login_required
def tarefa_delete(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        tarefa.delete()
        messages.success(request, 'Tarefa excluída com sucesso.')
        return redirect('admin_tarefas')
    return render(request, 'noticias/tarefa_confirm_delete.html', {'tarefa': tarefa})


def about(request):
    return render(request, 'noticias/about.html')


def contact(request):
    return render(request, 'noticias/contact.html')
