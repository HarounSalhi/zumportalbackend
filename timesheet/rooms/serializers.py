from rest_framework import serializers
from rooms.models import Room, Equipement ,RequestRooms

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room 
        fields = '__all__'

class EquipementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipement 
        fields = '__all__'

class RequestRoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestRooms 
        fields = '__all__'