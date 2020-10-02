from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('create/', views.todo_create, name='todo_create'),
    path('detail/<int:todo_id>', views.todo_detail, name='todo_detail'),
    path('update/<int:todo_id>', views.todo_update, name='todo_update'),
    path('delete/<int:todo_id>', views.todo_delete, name='todo_delete'),
]