from django.shortcuts import render, redirect
from django.contrib import messages


from .forms import TodoModelForm
from .models import TodoModel
# Create your views here.


def home_view(request):
    form = TodoModelForm()
    if request.method == 'POST':
        form = TodoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo:home')

    task_list = TodoModel.objects.order_by('date')
    total_tasks = len(TodoModel.objects.all())
    context = {
        'form' : form,
        'task_list' : task_list,
        'title' : 'TODO List',
        'total_tasks' : total_tasks,
    }
    return render(request, 'todo/home.html', context)


def delete_view(request, pk):
    task = TodoModel.objects.get(pk=pk)
    task.delete()
    messages.success(request, 'Task has been deleted.')

    return redirect('todo:home')

def clear_all(request):
    total = TodoModel.objects.all()
    total.delete()
    return redirect('todo:home')