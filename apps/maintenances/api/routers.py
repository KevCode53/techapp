# Imports Third Party
from rest_framework.routers import DefaultRouter

# Imports Views
from apps.maintenances.api.views.compromise_views import CompromiseViewSet
# from apps.users.api.views.user_views import UserViewSet

router = DefaultRouter()

router.register(r'compromises', CompromiseViewSet, basename='compromise')

urlpatterns = router.urls