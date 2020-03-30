from rest_framework import serializers
from assignment3.models import Card,Task

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(
        source='owner.username'
    )
    class Meta:
        model = Card
        fields = '__all__'
