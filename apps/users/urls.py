from django.urls import path
from apps.users.api.api_views import user_api_view, user_detail_view

urlpatterns = [
  path('users/', user_api_view, name='user'),
  path('users/<int:pk>', user_detail_view, name='user_update'),
]