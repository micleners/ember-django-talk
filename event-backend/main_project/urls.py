from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from events import views

# Two options for building out API endpoints
# 1. Loading in ViewSets using "default router"
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'events', views.EventViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    # 1(continued). Including this "default router" at the base of the API: localhost:4200
    path('api/', include(router.urls)),
    # 2. Including URLconf imported from `api` application, on api base url: localhost:4200/api
    path('api_verbose/', include('events.urls', namespace='api_verbose')),
]