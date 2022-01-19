from django.db import models

class TodoListItem(models.Model):
    text = models.CharField(max_length=50)
    complete = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
