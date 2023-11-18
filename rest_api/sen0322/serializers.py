from rest_framework import serializers
from .models import SEN0322

class SEN0322Serializer(serializers.ModelSerializer):
    class Meta:
        model = SEN0322
        fields = '__all__'

    def create(self, validated_data):
        return SEN0322.objects.create(**validated_data)
    
    def save(self):
        return super().save()
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'o2': instance.moisture,
            'time': instance.time
        }
    
    def serialize(self):
        return super().serialize()