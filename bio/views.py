from rest_framework.response import Response
from rest_framework import viewsets 
from bio import  models, serializers
from django.core import serializers as serialize
from rest_framework import status
from rest_framework.parsers import JSONParser

from rest_framework.decorators import api_view


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

@api_view(['POST'])
def arithmetic_view(request):
    data = JSONParser().parse(request)
    serializer = serializers.ArithmeticSerializer(data=data)
    if serializer.is_valid():
        x = serializer.data['x']
        y = serializer.data['y']
        operation_type = serializer.data['operation_type']

        if operation_type.lower() == 'addition':
            return Response({
                "slackUsername": "josephibochi",
                "result": x + y,
                "operation_type": 'addition'
            })
        elif operation_type.lower() == 'subtraction':
            return Response({
                "slackUsername": "josephibochi",
                "result": x - y,
                "operation_type": 'subtraction'
            })
        elif operation_type.lower() == 'multiplication':
            return Response({
                "slackUsername": "josephibochi",
                "result": x - y,
                "operation_type": 'multiplication'
            })
        else:
            raise ValueError("inappropriate operation_selection")