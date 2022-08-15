from rest_framework import generics

class GeneralListApiView(generics.ListAPIView):
    serializer_class = None

    def get_queryset(self):
      model = self.serializer_class.Meta.model.objects.all()
      return model