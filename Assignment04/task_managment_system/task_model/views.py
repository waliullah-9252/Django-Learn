from django.shortcuts import render,redirect
from .import forms
from .import models

# Create your views here.

def add_task(request):
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('add_task')
    else:
        task_form = forms.TaskForm()
    return render(request, 'task_model/add_task.html', {'form': task_form})

def edit_task(request,id):
    edit_tasks = models.TaskModel.objects.get(pk=id)
    task_form = forms.TaskForm(instance=edit_tasks)
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST, instance=edit_tasks)
        if task_form.is_valid():
            task_form.save()
            return redirect('homepage')

    return render(request, 'task_model/add_task.html', {'form': task_form})

def delete_task(request, id):
    delete_tasks = models.TaskModel.objects.get(pk = id).delete()
    return redirect('homepage')

def complete_task(request, id):
    complete_task = models.TaskModel.objects.get(pk=id)
    complete_task.is_complete = True
    complete_task.save()
    return redirect('homepage')