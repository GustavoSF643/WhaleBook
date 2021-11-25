from rest_framework import serializers

class ImageLinksSerializer(serializers.Serializer):
    smallThumbnail = serializers.CharField()
    thumbnail = serializers.CharField()

class VolumeInfoSerializer(serializers.Serializer):
    title = serializers.CharField()
    subtitle = serializers.CharField()
    authors = serializers.ListField()
    description = serializers.CharField()
    pageCount = serializers.IntegerField()
    categories = serializers.ListField()
    imageLinks = ImageLinksSerializer()
    language = serializers.CharField()

class BooksSerializer(serializers.Serializer):
    id = serializers.CharField()
    volumeInfo = VolumeInfoSerializer()
