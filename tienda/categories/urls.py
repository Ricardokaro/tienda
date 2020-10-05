
"""Categories URLs."""

# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

#Views
from .views import categories as category_views

router = DefaultRouter()
router.register(r'categories', category_views.CategoryViewSet, basename='category')

urlpatterns = [
    path("", include(router.urls))
]


