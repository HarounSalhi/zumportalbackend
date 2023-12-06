from rest_framework import serializers
from .models import Dayoff
from authentication.serializers import Registerserilaizer,userSerializer

class DayoffSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Dayoff
        fields = ['name','position','nbdays','type','createdate','startdate','returndate','backupperson','motif','creator','status','id']

class GetDayoffSerilaizer(serializers.ModelSerializer):
    # created_by = userSerializer(required = True)
    # assigned_to = userSerializer(many=True)
    class Meta:
        model = Dayoff
        fields = ['name','position','nbdays','type','createdate','startdate','returndate','backupperson','motif','creator','status','id']
        depth = 1



class GetAllDayoffSerilaizer(serializers.ModelSerializer):
    # assigned_to = userSerializer(many=True)
    created_by = userSerializer(required = True)

    class Meta:
        model = Dayoff
        fields = ['id','name','position','nbdays','type','createdate','startdate','returndate','backupperson','motif','creator','status']
        
class UpdateDayoffSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Dayoff
        fields = ('id','name','position','nbdays','type','createdate','startdate','returndate','backupperson','motif','creator','status')
        def update(self, instance, validated_data):
            instance.name = validated_data.pop('name', instance.name)
            instance.position = validated_data.pop('position', instance.position)
            instance.nbdays = validated_data.pop('nbdays', instance.nbdays)
            instance.type = validated_data.pop('type', instance.type)
            instance.createdate = validated_data.pop('createdate', instance.createdate)
            instance.startdate = validated_data.pop('startdate', instance.startdate)
            instance.returndate = validated_data.pop('returndate', instance.returndate)
            instance.backupperson = validated_data.pop('backupperson', instance.backupperson)
            instance.motif = validated_data.pop('motif', instance.motif)
            instance.creator = validated_data.pop('creator', instance.creator)
            instance.status = validated_data.pop('status', instance.status)

            instance.save()
            return instance
        
class ApprouveDayoffSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Dayoff
        fields = ('id','name','position','nbdays','type','createdate','startdate','returndate','motif','status')
        def update(self, instance, validated_data):
            instance.status = validated_data.pop('status', 'APPROVED')
            instance.save()
            return instance
        
class DeclineDayoffSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Dayoff
        fields = '__all__'
        def update(self, instance, validated_data):
            instance.status = validated_data.pop('status', 'DECLINED')
            instance.save()
            return instance


# class GetDayoffByUserSerilaizer(serializers.ModelSerializer):
#     created_by_id = Registerserilaizer
#     class Meta:
#         model = Dayoff
#         fields = ['id','name','position','nbdays','createdate','startdate','returndate','backupperson','motif','creator','status']


# class GetDayoffBycreatorSerilaizer(serializers.ModelSerializer):
#     class Meta:
#         model = Dayoff
#         fields = ['id','name','position','nbdays','createdate','startdate','returndate','backupperson','motif','creator','status']

   

# class GetDayoffBycreatorWithAffectedToSerilaizer(serializers.ModelSerializer):
#     assigned_to = UserAssginedToDayoffSerializer(many=True)
#     class Meta:
#         model = Dayoff
#         fields = ['id','name','position','nbdays','createdate','startdate','returndate','backupperson','motif','creator','status']


# class DayoffSerilaizerapprove(serializers.ModelSerializer):
#     class Meta:
#         model = Dayoff
#         fields = ['name', 'position', 'nbdays', 'type', 'createdate', 'startdate', 'returndate', 'backupperson', 'motif', 'creator', 'status', 'id']

#     def approve(self, instance):
#         instance.status = "APPROVED"
#         instance.save()

#     def update(self, instance, validated_data):
#         if 'status' in validated_data and validated_data['status'] == 'APPROVED':
#             self.approve(instance)
#         else:
#             instance = super().update(instance, validated_data)
#         return instance