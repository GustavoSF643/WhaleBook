from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.fields.related import ForeignKey

def validate_stars(value):
    if value < 1:
        raise ValidationError('Ensure this value is greater than or equal to 1.')
    if value > 10:
        raise ValidationError('Ensure this value is less than or equal to 10.')

class BookReview(models.Model):
    user = ForeignKey('accounts.User', on_delete=models.PROTECT, related_name='reviews')
    book_id = models.CharField(max_length=255)
    stars = models.IntegerField(validators=[validate_stars])
    review = models.TextField()