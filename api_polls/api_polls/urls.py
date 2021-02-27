from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API polls. From test task",
      default_version='v2',
      description="Api for work with polls.\n"
                  "Include QUESTIONS, ANSWERS, VOTES.\n"
                  "You can create poll and change his. Also you can delete it.",
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('admin/', admin.site.urls),
   path('rest-auth/', include('rest_auth.urls')),
   path('api/', include('poll.urls')),

]
