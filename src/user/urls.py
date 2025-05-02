from .views import home, UserRegisterView, UserLoginView, UserLogoutView
from django.urls import path

app_name = 'user'
urlpatterns = [
    path('', home, name='home'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]

