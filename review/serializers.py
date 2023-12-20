from rest_framework.fields import ReadOnlyField
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from review.models import Rating, Comment, FavouriteDriver, FavouriteLocation


class CommentSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.name')

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        comment = self.Meta.model.objects.create(author=user, **validated_data)
        return comment


class RatingSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.name')

    class Meta:
        model = Rating
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        rating = self.Meta.model.objects.create(author=user, **validated_data)
        return rating


class FavouritesSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.name')

    class Meta:
        model = FavouriteDriver
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        favourite = self.Meta.model.objects.create(author=user, **validated_data)
        return favourite

    def validate(self, attrs):
        driver = attrs.get('driver_profile')
        user = self.context.get('request').user
        if self.Meta.model.objects.filter(driver=driver, author=user).exists():
            raise serializers.ValidationError(
                'You already made this driver favourite'
            )
        return attrs


class FavouriteLocationSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.name')

    class Meta:
        model = FavouriteLocation
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        favourite = self.Meta.model.objects.create(author=user, **validated_data)
        return favourite

    def validate(self, attrs):
        location = attrs.get('location')
        user = self.context.get('request').user
        if self.Meta.model.objects.filter(location=location, author=user).exists():
            raise serializers.ValidationError(
                'You already made this location favourite'
            )
        return attrs

