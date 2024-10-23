from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .forms import AlunoForm
from .models import Aluno
from .filters import AlunoFilter

def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_alunos')
    else:
        form = AlunoForm()
    return render(request, 'alunos/cadastrar_aluno.html', {'form': form})


def editar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('listar_alunos')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'alunos/editar_aluno.html', {'form': form})

def listar_alunos(request):
    alunos = Aluno.objects.all()
    aluno_filter = AlunoFilter(request.GET, queryset=alunos)  # Aplica o filtro aos alunos
    return render(request, 'alunos/listar_alunos.html', {'aluno_filter': aluno_filter})