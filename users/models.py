from django.db import models
from django.contrib.auth.models import AbstractUser, Group
# from django.contrib.auth import get_user_model
# User = get_user_model()


class User(AbstractUser):
    groups = models.ForeignKey(Group, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50, unique=True)

    REQUIRED_FIELDS = ['groups_id', 'email']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'user'

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.username


class Event(models.Model):
    creator = models.CharField(max_length=255, blank=True, null=True)
    updator = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(
		auto_now_add=True, null=True, blank=True)
    updated_date = models.DateTimeField(
		auto_now_add=True, null=True, blank=True)
    name = models.CharField(max_length=100)
    venue = models.CharField(max_length=255, blank=True, null=True)
    date = models.CharField(max_length=20, blank=True, null=True)
    seats_count = models.IntegerField(default=0)
    booking_window = models.IntegerField(default=0)

class Ticket(models.Model):
    venue = models.CharField(max_length=255, blank=True, null=True)
    seat_number = models.IntegerField(default=0)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, default=0, related_name="event")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="tickets")


