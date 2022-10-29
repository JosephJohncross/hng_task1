from rest_framework.response import Response
from rest_framework import viewsets 
from bio import  models, serializers
from django.core import serializers as serialize
from rest_framework import status


class MyBioApiViewSet(viewsets.ModelViewSet):
    """Handles getting (creation and updating) my bio"""

    serializer_class = serializers.MyBioSerializer
    queryset = models.MyBio.objects.all()
    

    def list(self, request, *args, **kwargs):
        userExist = models.MyBio.objects.filter(id=1)
        if userExist:
            queryset = models.MyBio.objects.filter(id=1).values()
            data = queryset[0]
            data.pop('id')
            response = data

            if response is not None:
                return Response(response, status.HTTP_200_OK)
            else:
                response = {}
                return Response(response, status.HTTP_404_NOT_FOUND)
    