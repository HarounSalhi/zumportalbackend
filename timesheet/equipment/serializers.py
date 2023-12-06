from rest_framework import serializers
from .models import Equipment
from authentication.serializers import Registerserilaizer,userSerializer

class EquipmentSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['name','equipment','purpose','creator','createdate','startdate','endate','status','id']

class GetEquipmentSerilaizer(serializers.ModelSerializer):
    created_by = userSerializer(required = True)
    assigned_to = userSerializer(many=True)
    class Meta:
        model = Equipment
        fields = ['name','equipment','purpose','creator','createdate','startdate','endate','status','id']
        depth = 1



class GetAllEquipmentSerilaizer(serializers.ModelSerializer):
    assigned_to = userSerializer(many=True)
    created_by = userSerializer(required = True)

    class Meta:
        model = Equipment
        fields = ['id','name','equipment','purpose','creator','createdate','startdate','endate','status']

        
class UpdateEquipmentSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ('id','name','equipment','purpose','creator','createdate','startdate','endate','status')
        def update(self, instance, validated_data):
            instance.name = validated_data.pop('name', instance.name)
            instance.description = validated_data.pop('descreption', instance.description)
            instance.status = validated_data.pop('status', instance.status)
            instance.assigned_to = validated_data.pop('assigned_to', instance.assigned_to)
            instance.save()
            return instance


# class GetEquipmentByUserSerilaizer(serializers.ModelSerializer):
#     created_by_id = Registerserilaizer
#     class Meta:
#         model = Equipment
#         fields = ['id','name','equipment','purpose','creator','createdate','startdate','endate','status']


# class GetEquipmentBycreatorSerilaizer(serializers.ModelSerializer):
#     class Meta:
#         model = Equipment
#         fields = ['id','name','equipment','purpose','creator','createdate','startdate','endate','status']

   

# class GetEquipmentBycreatorWithAffectedToSerilaizer(serializers.ModelSerializer):
#     # assigned_to = Registerserilaizer
#     assigned_to = UserAssginedToEquipmentSerializer(many=True)
#     class Meta:
#         model = Equipment
#         fields = ['id','name','starter_at','description','status','end_date','assigned_to',]    


  