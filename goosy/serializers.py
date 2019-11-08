from rest_framework import serializers
from djangohomework.goosy.models import Track

# SnippetSerializer is inherit from serializers.ModelSerializer !!
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['id', 'track_title', 'track_author', 'track_album']