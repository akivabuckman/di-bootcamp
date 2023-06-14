from django.shortcuts import render
from .forms import TodoForm
from .models import Todo

def add_todo(request):
    if request.method == 'POST':
        filled_form = TodoForm(request.POST)
        if filled_form.is_valid():
           filled_form.save()
        else:
            print(filled_form.errors)
    todo_form = TodoForm()
    context = {'form': todo_form}
    return render(request, 'add_todo.html', context)


def display_todos(request):
    todos = Todo.objects.all()
    context = {'instances': todos}
    return render(request, 'todos.html', context)