from django.urls import path, include
from .views import ListToDoLists, ListToDoListItems, DetailToDoLists, DetailToDoListItems
from . import views


urlpatterns = [
    path('<int:pk', DetailToDoLists.as_view()),
    path('', ListToDoLists.as_view())
]


urlpatterns = [
    path('<int:pk', DetailToDoListItems.as_view()),
    path('',ListToDoListItems.as_view())
]
