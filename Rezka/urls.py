
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title='Rezka Rest API',
        default_version='v1',
        description='Rezka Rest API',
        terms_of_service="https://policies.google.com/",
        contact=openapi.Contact(
            name="Ilyas",
            url = "https://t.me/the_ilyas",
            email="thegg2022@gmail.com",
            ),
            license=openapi.License(
                name="MIT License",
                url="https://opensource.org/license/mit",
            ),
        ),
        public=True,
        permission_classes=[permissions.IsAdminUser]
)



urlpatterns = [
    path('admin', admin.site.urls),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/', include('apps.api.urls')),
]


