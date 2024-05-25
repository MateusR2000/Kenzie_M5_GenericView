from rest_framework import serializers
from albums.models import Album
from .models import Song


class SongSerializer(serializers.ModelSerializer):
    album_id = serializers.SerializerMethodField(read_only=True)

    def get_album_id(self, obj: Album):
        return obj.album.id

    class Meta:
        model = Song
        fields = ["id", "title", "duration", "album_id"]


