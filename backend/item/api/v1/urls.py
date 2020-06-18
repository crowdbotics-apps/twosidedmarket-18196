from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import CategoryViewSet, ItemViewSet, ReviewViewSet

router = DefaultRouter()
router.register("review", ReviewViewSet)
router.register("category", CategoryViewSet)
router.register("item", ItemViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
