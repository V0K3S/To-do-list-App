from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.


def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

class ToDoList(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def __get_absolute_url(self):
        return reverse("list", args=[self.id])
    
    
class ToDoListItem(models.Model):
    Title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    containing_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.Title}: due {self.due_date}"
    
    def get_absolute_url(self):
        return reverse(
            "item-update", args=[str(self.containing_list.id), str(self.id)]
            )
    