from apps.maintenances.models import Maintenance
from rest_framework import serializers

class MaintenanceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Maintenance
    exclude = ('state',)