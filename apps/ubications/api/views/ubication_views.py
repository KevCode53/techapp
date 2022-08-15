# Import Third Party
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

# Import Views
from apps.core.api.views.api import GeneralListApiView

# Import Serializers
from apps.ubications.api.serializers.ubications_serializer import UbicationListSerializer, UbicationSerializer

# List View
# class UbicationListApiView(GeneralListApiView):
#     serializer_class = UbicationListSerializer

#     def get_queryset(self):
#         return self.get_serializer().Meta.model.objects.all().filter(state=True)

# # Create View
# class UbicationCreateApiView(generics.CreateAPIView):
#     serializer_class = UbicationListSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Detail View
# class UbicationRetrieveApiView(generics.RetrieveAPIView):
#     serializer_class = UbicationListSerializer

#     def get_queryset(self):
#         return self.get_serializer().Meta.model.objects.filter(state=True)

#     # def get(self, request, pk=None, *args, **kwargs):

# # Delete View
# class UbicationDestroyApiView(generics.DestroyAPIView):
#     serializer_class = UbicationListSerializer

#     def get_queryset(self):
#         return self.get_serializer().Meta.model.objects.filter(state=True)

#     def delete(self, request, pk=None, *args, **kwargs):
#         ubication = self.get_queryset().filter(id = pk).first()
#         if ubication:
#             ubication.state = False
#             ubication.save()
#             return Response({'message': 'Ubication deleted succcessfull'}, status=status.HTTP_200_OK)
#         return Response({'message': 'Ubication not exists'}, status=status.HTTP_400_BAD_REQUEST)

# # Update View
# class UbicationUpdateApiView(generics.UpdateAPIView):
#     serializer_class = UbicationListSerializer

#     def get_queryset(self, pk):
#         return self.get_serializer().Meta.model.objects.filter(state=True).filter(id = pk).first()

#     def patch(self, request, pk=None, *args, **kwargs):

#         if self.get_queryset(pk):
#             ubication_serializer = self.serializer_class(self.get_queryset(pk))
#             # if serializer.is_valid():
#             #     serializer.save()
#             #     return Response(serializer.data, status=status.HTTP_200_OK)
#             # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#             return Response(ubication_serializer.data, status=status.HTTP_200_OK)
#         return Response({'message': 'Ubication not exists'}, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk=None, *args, **kwargs):
#         if self.get_queryset(pk):
#             ubication_serializer = self.serializer_class(self.get_queryset(pk), request.data, partial=True)
#             if ubication_serializer.is_valid():
#                 ubication_serializer.save()
#                 return Response(ubication_serializer.data, status=status.HTTP_200_OK)

#             return Response(ubication_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         return Response({'message': 'Ubication not exists'}, status=status.HTTP_400_BAD_REQUEST)

# List Create View
class UbicationCreateListApiView(generics.ListCreateAPIView):
    serializer_class = UbicationListSerializer
    queryset = UbicationSerializer.Meta.model.objects.filter(state=True)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Retrieve Update Destroy View
class UbicationRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UbicationListSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()
    
    def patch(self, request, pk=None, *args, **kwargs):

        if self.get_queryset(pk):
            ubication_serializer = self.serializer_class(self.get_queryset(pk))
            # if serializer.is_valid():
            #     serializer.save()
            #     return Response(serializer.data, status=status.HTTP_200_OK)
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(ubication_serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'Ubication not exists'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, *args, **kwargs):
        if self.get_queryset(pk):
            ubication_serializer = self.serializer_class(self.get_queryset(pk), request.data, partial=True)
            if ubication_serializer.is_valid():
                ubication_serializer.save()
                return Response(ubication_serializer.data, status=status.HTTP_200_OK)

            return Response(ubication_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'message': 'Ubication not exists'}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None, *args, **kwargs):
        ubication = self.get_queryset().filter(id = pk).first()
        if ubication:
            ubication.state = False
            ubication.save()
            return Response({'message': 'Ubication deleted succcessfull'}, status=status.HTTP_200_OK)
        return Response({'message': 'Ubication not exists'}, status=status.HTTP_400_BAD_REQUEST)