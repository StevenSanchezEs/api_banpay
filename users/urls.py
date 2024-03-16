from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, GhibliEndpointView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API documentation using Swagger",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('films/', GhibliEndpointView.as_view(endpoint='films'), name='films'),
    path('people/', GhibliEndpointView.as_view(endpoint='people'), name='people'),
    path('locations/', GhibliEndpointView.as_view(endpoint='locations'), name='locations'),
    path('species/', GhibliEndpointView.as_view(endpoint='species'), name='species'),
    path('vehicles/', GhibliEndpointView.as_view(endpoint='vehicles'), name='vehicles'),
    path('token_auth/', TokenObtainPairView.as_view(), name='token_auth'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]