from rest_framework import serializers
from .models import Order
from django.contrib.auth import get_user_model
from map.serializers import DistancesSerializer


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Order
        fields = '__all__'


User = get_user_model()


class OrderConfirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        order.in_stock = True
        order.save()
        return order

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['distances'] = DistancesSerializer(instance.comments.all(), many=True).data
        return rep
