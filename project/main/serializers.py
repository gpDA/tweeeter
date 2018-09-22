from rest_framework import serializers
from main.models import Main

class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = ('id', 'name', 'email', 'message')