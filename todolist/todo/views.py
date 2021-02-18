from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Todo
from django.shortcuts import get_object_or_404
from .forms import TodoForm


class TodoList(ListView):

    queryset = Todo.objects.all()
    template_name = "todo/list.html"


class TodoDetail(DetailView):

    queryset = Todo.objects.all()
    template_name = "todo/detail.html"


class TodoCreate(CreateView):

    form_class = TodoForm
    model = Todo
    template_name = "todo/form.html"
    extra_context = {"update": False}
