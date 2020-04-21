from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
# Create your views here.
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404

class MusicianListView(generics.ListCreateAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class MusicianView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MusicianSerializer
    queryset = Musician.objects.all()
        
class SongListView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SongSerializer
    queryset = Song.objects.all()
    
class SongList(APIView):
    serializer_class = SongSerializer
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, musician_pk, album_pk, format=None):
        album = Album.objects.get(id=album_pk)
        serializer = AlbumSerializer(instance=album)
        songs = serializer.data['song_album']
        return Response(songs)

    def post(self, request, musician_pk, format=None):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AlbumList(APIView):
    serializer_class = AlbumSerializer
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, musician_pk, format=None):
        musician = Musician.objects.get(id=musician_pk)
        serializer = MusicianSerializer(instance=musician)
        albums = serializer.data['album_musician']
        return Response(albums)

    def post(self, request, musician_pk, format=None):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AlbumDetail(APIView):
    serializer_class = AlbumSerializer
   
    def get(self, request, musician_pk, album_pk, format=None):
        musician = get_object_or_404(Musician, pk=musician_pk)
        album = AlbumSerializer(musician.album_musician.get(pk=album_pk))
        return Response(album.data)

    def post(self, request, musician_pk, album_pk, format=None):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, musician_pk, album_pk, format=None):
        album = Album.objects.get(id=album_pk)
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    def put(self, request, musician_pk, album_pk, format=None):
        album = Album.objects.get(pk=album_pk)
        data = request.data
        serializer = AlbumSerializer(instance=album, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class SongDetail(APIView):
    serializer_class = SongSerializer
    def get(self, request, musician_pk, album_pk, song_pk, format=None):
        album = get_object_or_404(Album, pk=album_pk)
        song = SongSerializer(album.song_album.get(pk=song_pk))
        return Response(song.data)

    def post(self, request, musician_pk, album_pk, song_pk, format=None):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, musician_pk, album_pk, song_pk, format=None):
        song = Song.objects.get(id=song_pk)
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    def put(self, request, musician_pk, album_pk, song_pk, format=None):
        song = Song.objects.get(pk=song_pk)
        data = request.data
        serializer = SongSerializer(instance=song, data=data)
        if serializer.is_valid():
            serializer.save()
