from rest_framework import serializers
from apps.ubications.models import Ubication

class UbicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubication
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

class UbicationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubication
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'code': instance.code,
            'name': instance.name,
            'address': instance.address,
            'phone': instance.phone,
            'department': instance.department.name,
            'estimated_computers': instance.estimated_computers,
        }
    
    def validate_estimated_computers(self, value):
        if value < 0:
            raise serializers.ValidationError("The estimated computers must be greater than 0")
        return value