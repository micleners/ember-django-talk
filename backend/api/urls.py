from .views import EventAPIView, EventRudView
from django.urls import path

app_name = "api"

# two URL paths that will be located on localhost:8000/api for option #2
urlpatterns = [
  path('events/', EventAPIView.as_view(), name='event-create'),
  path('events/<int:id>/', EventRudView.as_view(), name='event-detail')
]