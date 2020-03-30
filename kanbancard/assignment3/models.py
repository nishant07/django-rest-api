from django.db import models

class Card(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200,blank=True)
    STATUS_CHOICES = [('to-do','to-do'),('in-process','in-process'),('done','done'),]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    owner = models.ForeignKey('auth.User',related_name='cards',on_delete=models.CASCADE)

class Task(models.Model):
    card = models.ForeignKey(Card, related_name='tasks', on_delete=models.CASCADE)
    description = models.CharField(max_length=200,blank=False)
    done = models.BooleanField(default=False)

