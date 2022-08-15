from django.urls import path
from apps.ubications.api.views.ubication_views import (UbicationCreateListApiView, 
  UbicationRetrieveUpdateDestroyApiView)

urlpatterns = [
  path('ubication/', UbicationCreateListApiView.as_view(), name='ubication-list-create'),
  # path('ubication/retrieve/<int:pk>', UbicationRetrieveApiView.as_view(), name='ubication-retrieve'),
  # path('ubication/retrieve/<int:pk>', UbicationRetrieveApiView.as_view(), name='ubication-retrieve'),
  # path('ubication/destroy/<int:pk>', UbicationDestroyApiView.as_view(), name='ubication-destroy'),
  # path('ubication/update/<int:pk>', UbicationUpdateApiView.as_view(), name='ubication-update'),
  path('ubication/<int:pk>', UbicationRetrieveUpdateDestroyApiView.as_view(), name='ubication-retrieve-update-destroy'),
]
