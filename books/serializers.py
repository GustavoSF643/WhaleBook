from rest_framework import serializers

from books.models import BookReview

class ImageLinksSerializer(serializers.Serializer):
    smallThumbnail = serializers.CharField()
    thumbnail = serializers.CharField()

class VolumeInfoSerializer(serializers.Serializer):
    title = serializers.CharField()
    subtitle = serializers.CharField(required=False)
    authors = serializers.ListField(required=False)
    description = serializers.CharField(required=False)
    pageCount = serializers.IntegerField(required=False)
    categories = serializers.ListField(required=False)
    imageLinks = ImageLinksSerializer(required=False)
    language = serializers.CharField(required=False)

class BooksSerializer(serializers.Serializer):
    id = serializers.CharField()
    selfLink = serializers.CharField()
    volumeInfo = VolumeInfoSerializer()

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReview
        fields = ['id', 'user', 'book_id', 'stars', 'review']