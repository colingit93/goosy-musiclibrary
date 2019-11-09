from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from . import serializers
#from . import models

# Create your views here.
@api_view(['GET', 'POST'])
def list_tracks(request):
    """List all tracks"""
    if request.method == 'GET':
        tracks = models.Track.objects.all()
        serializer = serializers.TrackSerializer(tracks, many=True)
        return Response(serializer.data)

    # Data is send to the API
    elif request.method == 'POST':
        serializer = serializers.TrackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_track(request, pk):
    """
    Retreive, update or delete
    """

    try:
        tracks = models.Track.objects.get(pk=pk)
    except models.Track.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.TrackSerializer(tracks)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializers.TrackSerializer(tracks, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tracks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
