from django.db import models

class Card(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200,blank=True)
    STATUS_CHOICES = [('to-do','to-do'),('in-process','in-process'),('done','done'),]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
