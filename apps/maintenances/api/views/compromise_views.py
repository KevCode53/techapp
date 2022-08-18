# Imports Third Party
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

# Imports Serializers
from apps.maintenances.api.serializers.compromise_serializers import CompromiseCreateSerializer, CompromiseListSerializer

class CompromiseViewSet(viewsets.ModelViewSet):
  serializer_class = CompromiseListSerializer

  def get_queryset(self, pk=None):
    if pk:
      return self.get_serializer().Meta.model.objects.filter(state=True)
    return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

  # List all Compromises
  def list(self, request):
    # Obtiene todos los Compriomisos del año pasado y actual QuerySet
    queryset = CompromiseListSerializer.Meta.model.objects.all()
    # Serializa los Compromisos
    serializer = CompromiseListSerializer(queryset, many=True)
    # Retorna los Compromisos serializados
    return Response(serializer.data, status=status.HTTP_200_OK)
  

  # Create a new Compromise
  def create(self, request):
    # Serializa los datos enviados del Compromiso
    compromise_serializer = CompromiseCreateSerializer(data=request.data)
    # Verifica si el serializador es valido
    if compromise_serializer.is_valid():
      # Guarda el Compromiso
      compromise_serializer.save()
      # Retorna el Compromiso serializado
      return Response(compromise_serializer.data, status=status.HTTP_201_CREATED)
    # Retorna el error del serializador
    return Response(compromise_serializer.errors, status=status.HTTP_400_BAD_REQUEST)