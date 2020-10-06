from django.urls import path
from .views import addTask, allTask, viewTask, updateTask, deleteTask                                                                                                                                                                         

urlpatterns = [
    # API-URLS Paths 
    path('add-task/',               addTask,    name="AddTask"),
    path('all-task/',               allTask,    name="AllTask"),
    path('view-task/<str:pk>/',     viewTask,   name="ViewTask"),
    path('update-task/<str:pk>/',   updateTask,   name="ViewTask"),
    path('delete-task/<str:pk>/',   deleteTask,   name="ViewTask"),

]                                           
