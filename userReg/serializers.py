from rest_framework import serializers
from . import models

class dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.userData
        fields = ['username','password','email','avatar']

class weatherSerializer(serializers.Serializer):
    location = serializers.CharField()



