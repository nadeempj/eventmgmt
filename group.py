import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eventmgmt.settings')

import django

django.setup()
from django.contrib.auth.models import Group


GROUPS = ['admin', 'user']
MODELS = ['user']

for group in GROUPS:
    new_group, created = Group.objects.get_or_create(name=group)