from .models import Musician, Album, Song
from rest_framework import serializers


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'name', 'num_stars', 'from_album')


class AlbumSerializer(serializers.ModelSerializer):
    song_album = SongSerializer(read_only=True, many=True)

    class Meta:
        model = Album
        fields = (
                    'id',
                    'artist',
                    'name',
                    'release_date',
                    'num_stars',
                    'song_album'
                    )

    def create(self, validated_data):
        songs_data = None
        # use a try catch so that code doesn't break if there is no song data
        try:
            songs_data = validated_data.pop('song_album')
        except Exception as e:
            print(e)
        album = Album.objects.create(**validated_data)
        if songs_data is not None:
            for song_data in songs_data:
                Song.objects.create(album=album, **song_data)
        return album

    def update(self, instance, validated_data):
        songs_data = validated_data.pop('song_album')
        songs = (instance.song_album).all()
        songs = list(songs)
        instance.name = validated_data.get('name', instance.name)
        instance.num_stars = validated_data.get(
                                                'num_stars',
                                                instance.num_stars)
        instance.save()
        for song_data in songs_data:
            song = songs.pop(0)
            song.name = song_data.get('name', song.name)
            song.num_stars = song_data.get('num_stars', song.num_stars)
            song.save()
        return instance


class MusicianSerializer(serializers.ModelSerializer):
    album_musician = AlbumSerializer(read_only=True, many=True)

    class Meta:
        model = Musician
        fields = (
                    'id',
                    'first_name',
                    'last_name',
                    'instrument',
                    'album_musician'
                    )

    def create(self, validated_data):
        albums_data = None
        try:
            albums_data = validated_data.pop('album_musician')
        except Exception as e:
            print(e)
        musician = Musician.objects.create(**validated_data)
        if albums_data is not None:
            for album_data in albums_data:
                Album.objects.create(artist=musician, **album_data)
        return musician

    def update(self, instance, validated_data):
        albums_data = validated_data.pop('album_musician')
        albums = (instance.album_musician).all()
        albums = list(albums)
        instance.first_name = validated_data.get(
                                                'first_name',
                                                instance.first_name)
        instance.last_name = validated_data.get(
                                                'last_name',
                                                instance.last_name)
        instance.instrument = validated_data.get(
                                                'instrument',
                                                instance.instrument)
        instance.save()
        for album_data in albums_data:
            album = albums.pop(0)
            album.name = album_data.get('name', album.name)
            album.release_date = album_data.get(
                                                'release_date',
                                                album.release_date)
            album.num_stars = album_data.get('num_stars', album.num_stars)
            album.save()
        return instance
