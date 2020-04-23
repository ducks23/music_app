from apps.artists.models import Musician, Album, Song
from apps.artists.serializers import (
        MusicianSerializer,
        AlbumSerializer,
        SongSerializer
        )
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404


class MusicianListView(generics.ListCreateAPIView):
    '''
    list view for 'musicians/'
    '''
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class MusicianView(generics.RetrieveUpdateDestroyAPIView):
    '''
    detail view for 'musicians/<int:pk>'
    '''
    serializer_class = MusicianSerializer
    queryset = Musician.objects.all()


class AlbumList(APIView):
    '''
    list of albums for specified artist
    url: 'musicians/<int:pk>/albums
    '''
    serializer_class = AlbumSerializer
    
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
    '''
    detail of specified album in respect to musician 
    url: 'musicians/<int:pk>/albums/<int:pk>
    '''
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



class SongList(APIView):
    '''
    list of songs from album and artist
    url: musicians/<int:musician_pk>/albums/<int:album_pk>/songs/
    '''
    serializer_class = SongSerializer

    def get(self, request, musician_pk, album_pk, format=None):
        album = Album.objects.get(id=album_pk)
        serializer = AlbumSerializer(instance=album)
        songs = serializer.data['song_album']
        return Response(songs)

    def post(self, request, musician_pk, album_pk, format=None):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SongDetail(APIView):
    '''
    detail of specific song from album and artist
    url: musicians/<int:musician_pk>/albums/<int:album_pk>/songs/<int:song_pk>
    '''
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
