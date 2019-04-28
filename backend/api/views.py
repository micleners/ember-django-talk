from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics, mixins
from .models import Event
from .serializers import UserSerializer, GroupSerializer, EventSerializer


# No need to create models fro User and Group - they are baked into Django core
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

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

# 2. EventAPIView with create mixin and listview for frontend localhost:4200/events/ url
class EventAPIView(mixins.CreateModelMixin, generics.ListAPIView):
  resource_name = 'events'
  serializer_class = EventSerializer
  def get_queryset(self):
    return Event.objects.all()
  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

# 2(continued). Retrieve/Update/Delete view for frontend localhost:4200/events/[id] url
class EventRudView(generics.RetrieveUpdateDestroyAPIView):
  resource_name       = 'events'
  lookup_field        = 'id'
  serializer_class    = EventSerializer

  def get_queryset(self):
    return Event.objects.all()