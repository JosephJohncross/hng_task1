from rest_framework.response import Response
from rest_framework import viewsets 
from bio import  models, serializers


class MyBioApiViewSet(viewsets.ModelViewSet):
    """Handles getting (creation and updating) my bio"""

    serializer_class = serializers.MyBioSerializer
    queryset = models.MyBio.objects.all()

    def retrieve(self, request, *args, **kwargs):
        # ret = super(StoryViewSet, self).retrieve(request)
        return Response({'key': 'single value'})