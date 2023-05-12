
from django.contrib import admin
from django.urls import path, re_path, include
from mycare_backend import views
from rest_framework import permissions
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Tweet API",
        default_version='v1',
        description="Welcome to the world of Tweet",
        terms_of_service="https://www.tweet.org",
        contact=openapi.Contact(email="demo@tweet.org"),
        license=openapi.License(name="Awesome IP"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^doc(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),  # <-- 这里
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # <-- 这里
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # <-- 这里

    path('admin/', admin.site.urls),
    path('mycare/', include('mycare_backend.urls')),
]
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('mycare/', include('mycare_backend.urls')),
]
'''
