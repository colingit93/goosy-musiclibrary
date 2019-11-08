from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from djangohomework.goosy.models import Track
from djangohomework.goosy.serializers import SnippetSerializer
#from . import models

# Create your views here.
@api_view(['GET', 'POST'])
def list_tracks(request):
    """List all tracks"""
    if request.method == 'GET':
        tracks = Track.objects.all()
        serializer = SnippetSerializer(tracks, many=True)
        return Response(serializer.data)

    # Data is send to the API
    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
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
        tracks = Track.objects.get(pk=pk)
    except Track.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(tracks)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(tracks, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tracks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
