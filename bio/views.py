from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets 
from bio import  models, serializers


class MyBioApiViewSet(viewsets.ModelViewSet):
    """Handles getting (creation and updating) my bio"""

    serializer_class = serializers.MyBioSerializer
    queryset = models.MyBio.objects.all()