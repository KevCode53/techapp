# Imports Models
from apps.maintenances.models import Compromise

# Imports serializers
from apps.maintenances.api.serializers.general_serializers import CompromiseSerializer

# Imports Third Party
from rest_framework import generics

# Imports Views
from apps.core.api.views.api import GeneralListApiView

class CompromiseCreateAPIView(generics.CreateAPIView):
    queryset = Compromise.objects.all()
    serializer_class = CompromiseSerializer

class CompromiseListApiView(GeneralListApiView):
    serializer_class = CompromiseSerializer