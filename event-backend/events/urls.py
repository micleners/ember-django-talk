from .views import EventListView, EventDetailView
from django.urls import path

app_name = "api_verbose"

# two URL paths that will be located on localhost:8000/api_verbose for method #2
urlpatterns = [
  path('events/', EventListView.as_view(), name='event-list'),
  path('events/<int:id>/', EventDetailView.as_view(), name='event-detail')
]