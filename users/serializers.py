from asyncio import events
from datetime import datetime, timedelta
from pyexpat import model
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from users.models import Event, Ticket, User



class EventSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'creator', 'updator', 'created_date', 'updated_date', 'name', 'date', 'venue', 'seats_count', 'booking_window')
        model = Event
        extra_kwargs = {'id': {'read_only': True}, 
                        'created_date': {'read_only': True},
                        'updated_date': {'read_only': True}}

    def create(self, validated_data):
        event = Event.objects.create(**validated_data)
        event.creator = self.context['request'].user.username
        event.updator = self.context['request'].user.username
        event.save()
        return event

    def update(self, instance, validated_data):
        instance.booking_window = validated_data['booking_window']
        instance.name = validated_data['name']
        instance.seats_count = validated_data['seats_count']
        instance.date = validated_data['date']
        instance.venue = validated_data['venue']
        instance.updated_date = datetime.now()
        instance.save()
        return instance


class TicketSerializer(ModelSerializer):
    # event_name = CharField(source='Event.name')
    class Meta:
        fields = ('id', 'seat_number', 'event', 'user')
        read_only_fields = ('created','updated')
        model = Ticket

    def to_representation(self, instance):
        self.fields['event'] =  EventSerializer(read_only=True)
        return super(TicketSerializer, self).to_representation(instance)

    def create(self, validated_data):
        event_id = validated_data['event']
        # if event_id.created_date
        ticket = Ticket.objects.create(**validated_data)
        ticket.event.seats_count = ticket.event.seats_count - 1
        ticket.event.save()
        ticket.save()
        return ticket

class UserSerializer(ModelSerializer):
    # tickets = SerializerMethodField('_get_children')

    # def _get_children(self, obj):
    #     serializer = TicketSerializer(obj.child_list(), many=True)
    #     return serializer.data

    tickets = TicketSerializer(many=True, read_only=True)

    class Meta:
        fields = ('id', 'first_name', 'last_name', 'username', 'password', 'groups', 'email', 'tickets')
        # read_only_fields = ('tickets',)
        model = User
        extra_kwargs = {'password': {'write_only': True}}

    # def to_representation(self, instance):
    #     self.fields['tickets'] =  TicketSerializer(read_only=True)
    #     return super(UserSerializer, self).to_representation(instance)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.is_staff = True
        user.save()

        return user