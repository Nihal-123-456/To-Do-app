from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.views.generic.edit import CreateView
from django.views.generic import DeleteView
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
# Create your views here.


class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'form.html'

    def handle_no_permission(self):
        return redirect('user:home')

    def post(self, request, *args, **kwargs):
        task_form = self.form_class(data=request.POST)
        if task_form.is_valid():
            new_task = task_form.save(commit=False)
            new_task.user = self.request.user
            new_task.save()
            return redirect('user:home')
        return redirect('task:create_task')

@login_required
def task_complete_view(request, pk):
    task = get_object_or_404(Task, id=pk)
    if task.user == request.user:
        task.completed = True
        task.save()
        return redirect('user:home')
    return redirect('user:home')

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('user:home')

    def handle_no_permission(self):
        return redirect('user:home')