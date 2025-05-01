from django.shortcuts import render
from .forms import RegisterForm, LoginForm
from django.contrib.auth import get_user_model
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from task.models import Task
# Create your views here.

User = get_user_model()

def home(request):
    if request.user.is_authenticated:
        return render(request, 'index.html', {'object_list': Task.objects.filter(user=request.user)})
    return render(request, 'index.html')

class UserRegisterView(CreateView):
    model = User
    template_name = 'form.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home')

class UserLoginView(LoginView):
    template_name = 'form.html'
    form_class = LoginForm
    def get_success_url(self):
        return reverse_lazy('home')

class UserLogoutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('home')
