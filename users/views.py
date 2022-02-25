from datetime import datetime, timedelta
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import AllowAny
from users.permission import IsAdminUser, IsLoggedInUserOrAdmin, IsAdminOrUser, IsUser
from users.models import Event, Ticket, User
from users.serializers import EventSerializer, TicketSerializer, UserSerializer
import pandas as pd


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminUser]
        elif self.action == 'list':
            permission_classes = [IsAdminOrUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'destroy':
            permission_classes = [IsLoggedInUserOrAdmin]
        return [permission() for permission in permission_classes]


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminUser]
        elif self.action == 'list':
            permission_classes = [IsAdminOrUser]
        elif self.action == 'retrieve':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminUser]
        elif self.action == 'destroy':
            permission_classes = [IsLoggedInUserOrAdmin]
        return [permission() for permission in permission_classes]

    def retrieve(self, instance, *args, **kwargs):
        # do your customization here
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        # serializer.data['booking_window'] = str(serializer.data['created_date'] + timedelta(days=serializer.data['booking_window']))
        output = serializer.data
        output['booking_window'] = pd.to_datetime(serializer.data['created_date']) + timedelta(days=serializer.data['booking_window'])
        return Response(output)


class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsUser]
        elif self.action == 'list':
            permission_classes = [IsUser]
        elif self.action == 'retrieve':
            permission_classes = [IsUser]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminUser]
        elif self.action == 'destroy':
            permission_classes = [IsLoggedInUserOrAdmin]
        return [permission() for permission in permission_classes]

    # def retrieve(self, instance, *args, **kwargs):
    #     # do your customization here
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     # serializer.data['booking_window'] = str(serializer.data['created_date'] + timedelta(days=serializer.data['booking_window']))
    #     output = serializer.data
    #     output['booking_window'] = pd.to_datetime(serializer.data['created_date']) + timedelta(days=serializer.data['booking_window'])
    #     return Response(output)



class LoginView(ViewSet):
    serializer_class = AuthTokenSerializer

    def create(self, request):
        return ObtainAuthToken().as_view()(request=request._request)

class LogoutView(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)