from django.contrib import admin
from django.urls import path, include
from sos_rs_app.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('sos_rs_app.urls')),
    path('api/v2/', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
]
