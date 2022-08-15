from django.urls import path
from apps.maintenances.api.views.general_views import CompromiseListApiView, CompromiseCreateAPIView

urlpatterns = [
    path('compromises/', CompromiseListApiView.as_view(), name='compromise-list'),
    path('compromise_create/', CompromiseCreateAPIView.as_view(), name='compromise-create'),
]