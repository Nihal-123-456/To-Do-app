from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DeleteView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
# Create your views here.


class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'form.html'

    def handle_no_permission(self):
        return redirect('home')

    def post(self, request, *args, **kwargs):
        task_form = self.form_class(data=request.POST)
        if task_form.is_valid():
            new_task = task_form.save(commit=False)
            new_task.user = self.request.user
            new_task.save()
        return redirect('home')

@login_required
def task_complete_view(request, pk):
    try:
        task = Task.objects.get(id=pk)
        if task.user == request.user:
            task.completed = True
            task.save()
            return redirect('home')
        return redirect('home')
    except:
        return redirect('home')

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('home')

    def handle_no_permission(self):
        return redirect('home')