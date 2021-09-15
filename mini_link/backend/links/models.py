from django.db import models
from django.db.models.aggregates import Sum
from django.db.models.functions import ExtractMonth, ExtractDay, ExtractWeek
from django.db.models.deletion import CASCADE
from apps.users.models import User
from datetime import date, timedelta
from uuid import uuid4
from django.conf import settings


class Link(models.Model):
    url = models.URLField(null=False, blank=False)
    unique_token = models.UUIDField(
        primary_key=True, default=uuid4, editable=False, unique=True)
    tag = models.CharField(max_length=50, null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=CASCADE, null=True, blank=True)

    def link(self):
        '''returns usable shorted link '''
        return str(settings.DOMAIN)+"api/links/"+str(self.unique_token)

    def __str__(self):
        return self.url


class VisitManager(models.Manager):
    '''not implementd (Helpers for statss)'''
    def users_todays_visits(self):
        return self.filter(day=date.today()).aggregate(visits=Sum('count'))


class Visit(models.Model):
    '''visits stats'''
    link = models.ForeignKey(Link, blank=False, null=False, on_delete=CASCADE)
    count = models.PositiveIntegerField(default=1)

    objects = VisitManager()

    def __str__(self):
        return self.link.url
