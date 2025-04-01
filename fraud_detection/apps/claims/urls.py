from rest_framework.routers import DefaultRouter
from .views import ClaimViewSet

claims_router = DefaultRouter()
claims_router.register(r'claims', ClaimViewSet)
