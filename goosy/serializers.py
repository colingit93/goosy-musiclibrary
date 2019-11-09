from rest_framework import serializers
from . import models

# SnippetSerializer is inherit from serializers.ModelSerializer !!
class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Track
        fields = ['id', 'track_title', 'track_author', 'track_album']