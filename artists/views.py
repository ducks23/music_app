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


class MusicianListView(generics.ListCreateAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class MusicianView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MusicianSerializer
    queryset = Musician.objects.all()
        

class AlbumListView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    def get(self, request, musician_pk, format=None):
        musician = Musician.objects.get(id=musician_pk)
        serializer = MusicianSerializer(instance=musician)
        albums = serializer.data['album_musician']
        return Response(albums)


class AlbumView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()


class SongListView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SongSerializer
    queryset = Song.objects.all()
    

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
        print(musician_pk, album_pk)
        print('pkkkkkkkkkkkkkkkkkkkkkkkkk')
        try:
            musician = Musician.objects.get(id=musician_pk)
        except:
            print("no musician object found")
        serializer = MusicianSerializer(instance=musician)
        albums = serializer.data['album_musician']
        return Response(albums[album_pk])
    
    
    def post(self, request, musician_pk, album_pk, format=None):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, musician_pk, album_pk, format=None):
        album = Album.objects.get(pk=album_pk)
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    def put(self, request, musician_pk, album_pk, format=None):
        album = Album.objects.get(pk=album_pk)
        data = request.data
        serializer = AlbumSerializer(instance=album, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

