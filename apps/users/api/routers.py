# Imports Third Party
from rest_framework.routers import DefaultRouter

# Imports Views
from apps.users.api.views.user_views import UserViewSet

router = DefaultRouter()

router.register(r'users', UserViewSet, basename='user')

urlpatterns = router.urls