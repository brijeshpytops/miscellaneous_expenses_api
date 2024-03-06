from django.urls import path
from .views import taskListAPI
urlpatterns = [
    path('', taskListAPI, name='taskListAPI'),
]
