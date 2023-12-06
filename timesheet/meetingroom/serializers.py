from rest_framework import serializers
from .models import Meetingroom
from authentication.serializers import Registerserilaizer,userSerializer

class MeetingroomSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Meetingroom
        fields = ['name','room','purpose','creator','createdate','startdate','enddate','status','id']

class GetMeetingroomSerilaizer(serializers.ModelSerializer):
    created_by = userSerializer(required = True)
    assigned_to = userSerializer(many=True)
    class Meta:
        model = Meetingroom
        fields = ['name','room','purpose','creator','createdate','startdate','enddate','status','id']
        depth = 1



class GetAllMeetingroomSerilaizer(serializers.ModelSerializer):
    assigned_to = userSerializer(many=True)
    created_by = userSerializer(required = True)

    class Meta:
        model = Meetingroom
        fields = ['id','name','room','purpose','creator','createdate','startdate','enddate','status']

        
class UpdateMeetingroomSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Meetingroom
        fields = ('id','name','room','purpose','creator','createdate','startdate','enddate','status')
        def update(self, instance, validated_data):
            instance.name = validated_data.pop('name', instance.name)
            instance.description = validated_data.pop('descreption', instance.description)
            instance.status = validated_data.pop('status', instance.status)
            instance.assigned_to = validated_data.pop('assigned_to', instance.assigned_to)
            instance.save()
            return instance


# class GetMeetingroomByUserSerilaizer(serializers.ModelSerializer):
#     created_by_id = Registerserilaizer
#     class Meta:
#         model = Meetingroom
#         fields = ['id','name','room','purpose','creator','createdate','startdate','enddate','status']


# class GetMeetingroomBycreatorSerilaizer(serializers.ModelSerializer):
#     class Meta:
#         model = Meetingroom
#         fields = ['id','name','room','purpose','creator','createdate','startdate','enddate','status']

   

# class GetMeetingroomBycreatorWithAffectedToSerilaizer(serializers.ModelSerializer):
#     assigned_to = UserAssginedToMeetingroomSerializer(many=True)
#     class Meta:
#         model = Meetingroom
#         fields = ['id','name','room','purpose','creator','createdate','startdate','enddate','status']
  