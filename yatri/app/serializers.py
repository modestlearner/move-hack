from rest_framework import serializers
from .models import Todo, Aadhar, Vehicle


class TodoSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'destination', 'source', 'escore', 'type')


class AadhaarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aadhar
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'



