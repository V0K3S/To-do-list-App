from rest_framework import serializers
from .models import ToDoList
from .models import ToDoListItem

class ToDoListAppserializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ('Title', 'description', 'date_created', 'last_updated')
        
    class Meta:
        model = ToDoListItem
        fields = ('Title', 'description', 'date_created', 'due_date', 'containing_list' )