from django.shortcuts import render
from .forms import RegisterForm, LoginForm
from django.contrib.auth import get_user_model
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from task.models import Task
from django.contrib import messages
from django.shortcuts import redirect
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
    success_url = reverse_lazy('user:home')

    def post(self, request):
        user_form = self.form_class(data=request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(self.request,'Registration Completed. Now please login.')
            return redirect('user:login')
        return redirect('user:register')

class UserLoginView(LoginView):
    template_name = 'form.html'
    form_class = LoginForm
    def get_success_url(self):
        return reverse_lazy('user:home')

class UserLogoutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('user:home')
