# Imports Third Party
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

# Imports Serializers
from apps.users.api.serializers.user_serializers import UserSerializer, UserListSerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [authentication.TokenAuthentication]

    def get_queryset(self, pk=None):
        if pk:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    # List all users
    def list(self, request): 
        # Obtiene todos los usuarios QuerySet
        queryset = UserListSerializer.Meta.model.objects.all().values('id', 'nip', 'username', 'password', 'email', 'name', 'last_name', 'is_active')
        # Serializa los usuarios
        serializer = UserListSerializer(queryset, many=True)
        # Retorna los usuarios serializados
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Create a new user
    def create(self, request):
        # Serializa los datos enviados del usuario
        user_serializer = UserSerializer(data=request.data)
        # Verifica si el serializador es valido
        if user_serializer.is_valid():
            # Guarda el usuario
            user_serializer.save()
            # Retorna el usuario serializado
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        # Retorna el error del serializador
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


