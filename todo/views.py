from django.shortcuts import render, redirect
from .models import TodoList
from .forms import TodoListForm

def todo_list(request):
    context = {
        'todo_list': TodoList.objects.all(),
    }
    return render(request, 'todo/todo_list.html', context)

def todo_create(request):
    if request.method == 'GET':
        context = {
            'form': TodoListForm(),
        }
        return render(request, 'todo/todo_form.html', context)
    else:
        form = TodoListForm(request.POST)
        form.save()
        return redirect('todo:todo_list')

def todo_detail(request, todo_id):
    context = {
        'todo': TodoList.objects.get(id=todo_id),
    }
    return render(request, 'todo/todo_detail.html', context)

def todo_update(request, todo_id):
    if request.method == 'GET':
        todo = TodoList.objects.get(id=todo_id)
        form = TodoListForm(instance=todo)
        context = {
            'form': form,
        }
        return render(request, 'todo/todo_form.html', context)
    else:
        todo = TodoList.objects.get(id=todo_id)
        form = TodoListForm(request.POST, instance=todo)  #instance
        form.save()
        return redirect('todo:todo_list')

def todo_delete(request, todo_id):
    if request.method == 'GET':
        context = {
            'todo': TodoList.objects.get(id=todo_id),
        }
        return render(request, 'todo/todo_confirm_delete.html', context)
    else:
        todo = TodoList.objects.get(id=todo_id)
        todo.delete()
        return redirect('todo:todo_list')

