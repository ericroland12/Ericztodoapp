from django.shortcuts import render
from .models import TodoListItem


def todoappView(request):
    all_todo_items = TodoListItems.objects.all()
    return render(request, 'index.html',
    {'all_items': all_todo_items})

