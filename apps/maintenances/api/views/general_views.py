# Imports Models
from apps.maintenances.models import Compromise

# Imports serializers
from apps.maintenances.api.serializers.general_serializers import CompromiseSerializer

# Imports Third Party
from rest_framework import generics

class CompromiseCreateAPIView(generics.CreateAPIView):
    queryset = Compromise.objects.all()
    serializer_class = CompromiseSerializer

class CompromiseListAPIView(generics.ListAPIView):
    serializer_class = CompromiseSerializer

    def get_queryset(self):
      return Compromise.objects.filter(state=True)