from django.shortcuts import render
from rest_framework import generics 
from .serializers import ToDoListAppserializer
from .models import ToDoList, ToDoListItem

class ListToDoLists(generics.ListAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListAppserializer
    
class ListToDoListItems(generics.ListAPIView):
    queryset = ToDoListItem.objects.all()
    serializer_class = ToDoListAppserializer
    
class DetailToDoLists(generics.RetrieveAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListAppserializer

class DetailToDoListItems(generics.RetrieveAPIView):
    queryset = ToDoListItem.objects.all()
    serializer_class = ToDoListAppserializer


