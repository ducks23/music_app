from .models import *
from rest_framework import serializers, fields

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'from_album',  'name', 'num_stars')

class AlbumSerializer(serializers.ModelSerializer):
    song_album = SongSerializer(read_only=True, many=True)
    class Meta:
        model = Album
        fields = ('id', 'artist', 'name', 'release_date', 'num_stars', 'song_album')
    def create(self, validated_data):
        songs_data = None
        #use a try catch so that code doesn't break if there is no song data
        try:
            songs_data = validated_data.pop('song_from_album')
        except:
            print("key error for song data")
        album = Album.objects.create(**validated_data)
        if songs_data != None:
            for song_data in songs_data:
                Song.objects.create(album=song, **song_data)
        return album


class MusicianSerializer(serializers.ModelSerializer):
    album_musician = AlbumSerializer(read_only=True, many=True)
    class Meta:
        model = Musician
        fields = ('id', 'first_name', 'last_name', 'instrument', 'album_musician')

    def create(self, validated_data):
        albums_data = None
        try:
            albums_data = validated_data.pop('album_musician')
        except:
            print("key error")
        musician = Musician.objects.create(**validated_data)
        if albums_data != None:
            for album_data in albums_data:
                Album.objects.create(artist=musician, **album_data)
        return musician

    def update(self, instance, validated_data):
        albums_data = validated_data.pop('album_musician')
        albums = (instance.album_musician).all()
        albums = list(albums)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.instrument = validated_data.get('instrument', instance.instrument)
        instance.save()

        for album_data in albums_data:
            album = albums.pop(0)
            album.name = album_data.get('name', album.name)
            album.release_date = album_data.get('release_date', album.release_date)
            album.num_stars = album_data.get('num_stars', album.num_stars)
            album.save()
        return instance

from rest_framework.reverse import reverse

class CustomerHyperlink(serializers.HyperlinkedRelatedField):
    view_name = 'album-detail'
    queryset = Album.objects.all()

    def get_url(self, obj, view_name, request, format):
        print(obj, view_name, request)
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        url_kwargs = {
            'pk': obj.artist.pk,
            'album_pk': obj.pk
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

    def get_object(self, view_name, view_args, view_kwargs):

        lookup_kwargs = {
           '_pk': view_kwargs['pk'],
           'album_pk': view_kwargs['album_pk']
        }
        print("oooooooooooooooooooooooooooooooooo")
        print(lookup_kwargs)
        return self.get_queryset().get(**lookup_kwargs) 
