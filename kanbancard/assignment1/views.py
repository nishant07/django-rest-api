from django.shortcuts import render
from assignment1.models import Card
from assignment1.serializers import CardSerializer
from rest_framework import generics

class CardCollection(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class CardItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
