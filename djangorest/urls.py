from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    #biblioteca
    path('biblioteca/', include('apps_content.biblioteca.urls')),
    #users
    path('users/', include('apps_content.users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    #accoints
    path('accounts/', include('allauth.urls')),  # new
    #apirest
    path('api/', include('apps_content.api.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
