from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .fftactics_api import views

router = routers.DefaultRouter()
router.register(r'jobs', views.JobViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
