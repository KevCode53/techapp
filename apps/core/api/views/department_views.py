# Imports Third Party
# from rest_framework.generics import ListAPIView

# Imports serializers
from apps.core.api.serializers.department_serializers import DepartmentSerializer

# Import Views
from .api import GeneralListApiView

class DepartmentListAPIView(GeneralListApiView):
  serializer_class = DepartmentSerializer