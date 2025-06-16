from django.urls import path
from tasks.views import TaskListView, ChangeStateView

urlpatterns = [
    path('tareas/', TaskListView.as_view(), name='tarea-list'),
    path('tareas/<int:pk>/cambiar-estado/', ChangeStateView.as_view(), name='cambiar-estado'),
]