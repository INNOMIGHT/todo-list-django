from .views import TodoList, TodoDetail, TodoCreate
from django.urls import path


urlpatterns = [
    path("todos/", TodoList.as_view(), name="todo-list"),
    path("todos/add/", TodoCreate.as_view(), name="todo-create"),
    path("todos/<str:slug>/", TodoDetail.as_view(), name="todo-detail"),
]
