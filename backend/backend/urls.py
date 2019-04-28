from django.urls import include, path
from rest_framework import routers
from api import views

# Two options for building out API endpoints
# 1. Loading in ViewSets using "default router"
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'events', views.EventViewSet)

urlpatterns = [
# 1(continued). Including this "default router" at the base of the API: localhost:4200
    path('', include(router.urls)),
# 2. Including URLconf imported from `api` application, on api base url: localhost:4200/api
    path('api/', include('api.urls', namespace='api-events')),
]
