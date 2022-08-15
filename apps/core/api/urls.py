from django.urls import path
from apps.core.api.views.department_views import DepartmentListAPIView
urlpatterns = [
    path('departments/', DepartmentListAPIView.as_view(), name='department_list'),
]