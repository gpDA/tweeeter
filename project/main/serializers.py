from rest_framework import serializers
from main.models import Tweet

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        exclude = []
