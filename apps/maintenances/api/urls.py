from django.urls import path
from apps.maintenances.api.views.general_views import CompromiseListAPIView, CompromiseCreateAPIView

urlpatterns = [
    path('compromise/', CompromiseListAPIView.as_view(), name='compromise-list'),
    path('compromise/', CompromiseCreateAPIView.as_view(), name='compromise-create'),
]