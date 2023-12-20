from rest_framework.serializers import ModelSerializer
from .models import Locations, Distances


class LocationsSerializer(ModelSerializer):
    class Meta:
        model = Locations
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['favourite_location'] = instance.favourites.count()
        return rep


class DistancesSerializer(ModelSerializer):
    class Meta:
        model = Distances
        fields = '__all__'