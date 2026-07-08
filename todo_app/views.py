from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    form = TaskForm()

    context = {
        'tasks': tasks,
        'form': form
    }

    return render(request, 'todo/index.html', context)


def update_task(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('/')

    return render(request, 'todo/update.html', {'task': task})


def delete_task(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    return render(request, 'todo/delete.html', {'task': task})
