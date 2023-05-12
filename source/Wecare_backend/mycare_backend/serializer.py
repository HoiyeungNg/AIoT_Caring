from datetime import datetime

from rest_framework import serializers
from .models import TempInfo, HeartInfo, BodyStatusInfo


class TempSerializer(serializers.Serializer):
    temperature = serializers.DecimalField(max_digits=6, decimal_places=2)
    update_time = serializers.DateTimeField()

    def create(self, validated_data):
        return TempInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.temperature = validated_data.get('temperature', instance.temperature)
        instance.update_time = validated_data.get('update_time', instance.update_time)
        instance.save()
        return instance



class HeartSerializer(serializers.Serializer):
    heart_rate = serializers.DecimalField(max_digits=6, decimal_places=2)
    update_time = serializers.DateTimeField()

    def create(self, validated_data):
        return HeartInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.heart_rate = validated_data.get('heart_rate', instance.heart_rate)
        instance.update_time = validated_data.get('update_time', instance.update_time)
        instance.save()
        return instance



class BodyStatusSerializer(serializers.Serializer):
    body_status = serializers.CharField(max_length=10)
    update_time = serializers.DateTimeField()

    def create(self, validated_data):
        return BodyStatusInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.body_status = validated_data.get('body_status', instance.body_status)
        instance.update_time = validated_data.get('update_time', instance.update_time)
        instance.save()
        return instance


