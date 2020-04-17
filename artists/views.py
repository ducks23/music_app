from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
# Create your views here.
from rest_framework.response import Response

class MusicianListView(generics.ListCreateAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class MusicianView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MusicianSerializer
    queryset = Musician.objects.all()


class AlbumListView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()


class SongListView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SongSerializer
    queryset = Song.objects.all()

@api_view(['GET', 'PUT', 'DELETE'])
def album_detail(request, musician_pk, album_pk):
    '''
    this gets album detail with a specific artist in mind
    '''

    if request.method == 'GET':
        try:
            musician = Musician.objects.get(id=musician_pk)
        except:
            print("no musician object found")
        serializer = MusicianSerializer(instance=musician)
        albums = serializer.data['album_musician']
        print(albums[album_pk])
        return Response(albums[album_pk])

