from rest_framework import serializers
from apps.maintenances.models import Compromise

class CompromiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compromise
        exclude = ('state', 'created_date',)