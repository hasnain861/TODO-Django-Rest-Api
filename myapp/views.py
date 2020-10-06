from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import UserSerializer, TaskSerializer
from .models import Task

# ------------------------ C R U D --------------------------- #  

#CREATE
@api_view(['POST'])
def addTask(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({'msg':'Task successfully added !'})
# ------------------------------------------------------------

#READ
@api_view(['GET'])
def allTask(request):
    all_task = Task.objects.all()
    serializer = TaskSerializer(all_task, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def viewTask(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({'msg':'Invalid Task ID Number !'})

    if task:
        serializer = TaskSerializer(task, many=False)

    return Response(serializer.data)
# ---------------------------------------------------

#UPDATE
@api_view(['POST'])
def updateTask(request, pk):
    try:
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Task successfully UPDATED !'})
    except Task.DoesNotExist:
        return Response({'msg':'Invalid Task ID Number !'})

# -----------------------------------------------------------------

#DELETE
@api_view(['DELETE'])
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response({'msg':'Task successfully Deleted !'})

    
