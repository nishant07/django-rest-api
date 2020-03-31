from django.shortcuts import render
from assignment3.models import Card, Task
from assignment3.serializers import CardSerializer, TaskSerializer
from rest_framework import generics
from rest_framework import generics, permissions
from django.core import exceptions
from assignment3.custom_permissions import IsOwner, IsCardOwner

class CardCollection(generics.ListCreateAPIView):
    # queryset = Card.objects.all()
    serializer_class = CardSerializer

    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Card.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CardItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

class TaskCollection(generics.ListCreateAPIView):
    # queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsCardOwner]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        if serializer.validated_data['card'].owner != self.request.user:
            raise exceptions.PermissionDenied
        else:
            serializer.save()

class TaskItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsCardOwner]
