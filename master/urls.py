from django.urls import path
from .views import taskListAPI,taskDetailAPI
urlpatterns = [
    path('', taskListAPI, name='taskListAPI'),
    path('task/<int:task_id>', taskDetailAPI, name='taskDetailAPI')
]
