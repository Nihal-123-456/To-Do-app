from django.urls import path
from .views import TaskCreateView, task_complete_view, TaskDeleteView

app_name='task'
urlpatterns = [
    path('create/', TaskCreateView.as_view(), name='create_task'),
    path('<int:pk>/complete/', task_complete_view, name='complete_task'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='delete_task')
]
