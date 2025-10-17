from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm

# Create your views here.

# def task_list(request):
#     tasks = Task.objects.all()
#     return render(request, 'tasks/task_list.html',{'tasks': tasks})

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_edit.html'
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        #Adicionar lógica se necessário
        return super().form_valid(form)
    
class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/task_delete.html"
    success_url = reverse_lazy('task-list')