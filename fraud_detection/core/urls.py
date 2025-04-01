from django.urls import path, include
from apps.claims.urls import claims_router
from apps.users.urls import users_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(claims_router.urls)),
    path('api/', include(users_router.urls)),
]
