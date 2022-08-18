from rest_framework import serializers
from apps.maintenances.models import Compromise
from ....ubications.models import Ubication

class CompromiseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compromise
        exclude = ('state', 'created_date',)


class CompromiseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compromise
        exclude = ('state', 'created_date',)
    
    def to_representation(self, instance):
        # Creamos una variable 
        users = []
        for u in instance.users.all():
            users.append(u.name)
        ubications = []
        for u in instance.ubications.all():
            ubications.append(u.name)
        return {
            'id': instance.id,
            'year': instance.year,
            'users': users,
            'ubications': ubications, 
            'estimated_computers': instance.estimated_computers,
            'total_computers': instance.total_computers,
        }