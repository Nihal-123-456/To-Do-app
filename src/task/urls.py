from django.urls import path
from .views import TaskCreateView, task_complete_view, TaskDeleteView

urlpatterns = [
    path('task_create/', TaskCreateView.as_view(), name='create_task'),
    path('complete_task/<int:pk>/', task_complete_view, name='complete_task'),
    path('delete_task/<int:pk>', TaskDeleteView.as_view(), name='delete_task')
]
