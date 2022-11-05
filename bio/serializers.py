from dataclasses import fields
from rest_framework import serializers

from bio import  models

class MyBioSerializer(serializers.ModelSerializer):
    """Serializes bio information"""

    class Meta:
        model = models.MyBio
        fields = ('slackUsername', 'backend', 'age', 'bio')

class ArithmeticSerializer(serializers.Serializer):
    x = serializers.IntegerField()
    y = serializers.IntegerField()
    operation_type = serializers.CharField(max_length=50)

    