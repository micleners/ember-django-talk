from django.contrib.auth.models import User
from rest_framework import viewsets, generics, mixins
from .models import Event
from .serializers import UserSerializer, EventSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

# Two options for building up Event serializer - simpler or more complex
# Both option yield same result - could there be any benefits for using the second option?
# 1. ModelViewSet contians all the functionality present in two Views below
class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    resource_name = 'events'
    queryset = Event.objects.all()
    serializer_class = EventSerializer

# 2. EventListView with create mixin and listview for frontend localhost:4200/events/ url
class EventListView(mixins.CreateModelMixin, generics.ListAPIView):
  resource_name = 'events'
  serializer_class = EventSerializer
  def get_queryset(self):
    return Event.objects.all()
  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

# 2(continued). Retrieve/Update/Delete view for frontend localhost:4200/events/[id] url
class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
  resource_name       = 'events'
  lookup_field        = 'id'
  serializer_class    = EventSerializer

  def get_queryset(self):
    return Event.objects.all()