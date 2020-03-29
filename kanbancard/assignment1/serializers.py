from rest_framework import serializers
from assignment1.models import Cards

class CardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = '_all_'
