from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework import authentication
from rest_framework.response import Response
from rest_framework import status
from .models import Link,Visit
from .serializers import (linksReadSerializers,linksGuestWriteSerializers
,VisitReadSerialzer,VisitWriteSerialzer)


class LinkCreator(APIView):
    """
    Create and list links for guests.
    """
    serializer_class = linksGuestWriteSerializers
    queryset = Link.objects.all()

    def post(self, request,*args, **kwargs):
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            url=Link.objects.create(**request.data)
            return Response({'url': url.link()})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class UserLinkCreator(APIView):
    """
    Create and list links for users. (Not Implemented)
    """
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request, format=None):
        return Response({}, 200)

    def post(self, request, format=None):
        return




class EngagementList(APIView):
    """
    total engament today. (Not Implemented)
    """

    def get(self, request, format=None):
        return


class RedirectToDestination(APIView):
    """
    Redirects to Destination Url
    """
    queryset = Link.objects.all()
    def get(self, request, token):
        url = Link.objects.get(unique_token=token)
        visitsTracker = Visit.objects.get_or_create(link=url)

        if not visitsTracker:
            visitsTracker.count = visitsTracker.count + 1
            visitsTracker.save()
        return redirect(url.url)
