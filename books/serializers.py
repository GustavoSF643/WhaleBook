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
    averageRating = serializers.FloatField()

class BooksSerializer(serializers.Serializer):
    id = serializers.CharField()
    selfLink = serializers.CharField()
    volumeInfo = VolumeInfoSerializer()

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReview
        fields = ['id', 'user', 'book_id', 'stars', 'review']
        read_only_fields = ['user', 'book_id']
        extra_kwargs = {'review': {'required': False}}

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        validated_data['book_id'] = self.context['view'].kwargs.get('book_id')
        return super().create(validated_data)