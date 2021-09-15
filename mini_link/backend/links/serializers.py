from typing import Counter
from rest_framework import serializers
from .models import Link, Visit

class linksReadSerializers(serializers.Serializer):
    '''Read links (used in stats ) --not implementd--'''
    class Meta:
        model = Link
        fields = 'all'
        


class linksGuestWriteSerializers(serializers.Serializer):
    '''url creation'''
    url = serializers.CharField()

    def create(self, validated_data):
        return Link(**validated_data)



class VisitReadSerialzer(serializers.Serializer):
    '''Read visits (used in stats ) --not implementd--'''
    link = serializers.CharField()
    count = serializers.IntegerField()
    day = serializers.DateField()


class VisitWriteSerialzer(serializers.Serializer):
    '''modifies and adds links (used in stats ) --not implementd--'''

    link = serializers.CharField()
    count = serializers.IntegerField()
    day = serializers.DateField()

    def create(self, validated_data):
        return Visit(**validated_data)

    def update(self, instance, validated_data):
        #check for the uuid and date
        #if exist add one to count
        #else create new record
        return
