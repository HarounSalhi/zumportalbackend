from rest_framework import serializers
from .models import Remotework
from .models import Remoteworkplan
from authentication.serializers import Registerserilaizer,userSerializer

class RemoteworkplanSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Remoteworkplan
        fields = ['date', 'task', 'status']

    def create(self, validated_data):
        # Get the related Remotework instance from the context.
        remotework_instance = self.context['remotework_instance']
        print(remotework_instance)
        # Automatically set the 'request' field to the ID of the related Remotework.
        validated_data['request'] = remotework_instance.id

        # Create and return the Remoteworkplan instance.
        return Remoteworkplan.objects.create(**validated_data)

class GetRemoteworkplanSerilaizer(serializers.ModelSerializer):
    created_by = userSerializer(required = True)
    assigned_to = userSerializer(many=True)
    class Meta:
        model = Remoteworkplan
        fields = ['date', 'task', 'status', 'request', 'id']
        depth = 1



class GetAllRemoteworkplanSerilaizer(serializers.ModelSerializer):
    assigned_to = userSerializer(many=True)
    created_by = userSerializer(required = True)

    class Meta:
        model = Remoteworkplan
        fields = ['id','name','description','status','starter_at','created_by','assigned_to','end_date',]

        
class UpdateRemoteworkplanSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Remoteworkplan
        fields = ('id','name','description','status','starter_at','created_by','assigned_to','end_date',)
        def update(self, instance, validated_data):
            instance.name = validated_data.pop('name', instance.name)
            instance.description = validated_data.pop('descreption', instance.description)
            instance.status = validated_data.pop('status', instance.status)
            instance.assigned_to = validated_data.pop('assigned_to', instance.assigned_to)
            instance.save()
            return instance


# class GetRemoteworkplanByUserSerilaizer(serializers.ModelSerializer):
#     created_by_id = Registerserilaizer
#     class Meta:
#         model = Remoteworkplan
#         fields = ['id','name','starter_at','description','status','end_date','created_by_id',]


# class GetRemoteworkplanBycreatorSerilaizer(serializers.ModelSerializer):
#     class Meta:
#         model = Remoteworkplan
#         fields = ['id','name','starter_at','description','status','end_date',]    

   

# class GetRemoteworkplanBycreatorWithAffectedToSerilaizer(serializers.ModelSerializer):
#     assigned_to = UserAssginedToRemoteworkplanSerializer(many=True)
#     class Meta:
#         model = Remoteworkplan
#         fields = ['id','name','starter_at','description','status','end_date','assigned_to',]    

class RemoteworkSerilaizer(serializers.ModelSerializer):
    remotework_plans = RemoteworkplanSerilaizer()

    class Meta:
        model = Remotework
        fields = ['name','position','nbdays','createdate','startdate','returndate','motif','creator','status','id','remotework_plans']

class GetRemoteworkSerilaizer(serializers.ModelSerializer):
    # created_by = userSerializer(required = True)
    # assigned_to = userSerializer(many=True)
    class Meta:
        model = Remotework
        fields = ['name','position','nbdays','createdate','startdate','returndate','motif','creator','status','id']
        depth = 1



class GetAllRemoteworkSerilaizer(serializers.ModelSerializer):
    # assigned_to = userSerializer(many=True)
    # created_by = userSerializer(required = True)

    class Meta:
        model = Remotework
        fields = ['id','name','position','nbdays','createdate','startdate','returndate','motif','creator','status']

        
class UpdateRemoteworkSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Remotework
        fields = ('id','name','position','nbdays','createdate','startdate','returndate','motif','creator','status')
        def update(self, instance, validated_data):
            instance.id = validated_data.pop('id', instance.id)
            instance.name = validated_data.pop('name', instance.name)
            instance.position = validated_data.pop('position', instance.position)
            instance.nbdays = validated_data.pop('nbdays', instance.nbdays)
            instance.createdate = validated_data.pop('createdate', instance.createdate)
            instance.startdate = validated_data.pop('startdate', instance.startdate)
            instance.returndate = validated_data.pop('returndate', instance.returndate)
            instance.motif = validated_data.pop('motif', instance.motif)
            instance.creator = validated_data.pop('creator', instance.creator)
            instance.status = validated_data.pop('status', instance.status)

            instance.save()
            return instance


# class GetRemoteworkByUserSerilaizer(serializers.ModelSerializer):
#     created_by_id = Registerserilaizer
#     class Meta:
#         model = Remotework
#         fields = ['id','name','position','nbdays','createdate','startdate','returndate','motif','creator','status']


# class GetRemoteworkBycreatorSerilaizer(serializers.ModelSerializer):
#     class Meta:
#         model = Remotework
#         fields = ['id','name','position','nbdays','createdate','startdate','returndate','motif','creator','status']

   

# class GetRemoteworkBycreatorWithAffectedToSerilaizer(serializers.ModelSerializer):
#     assigned_to = UserAssginedToRemoteworkSerializer(many=True)
#     class Meta:
#         model = Remotework
#         fields = ['id','name','position','nbdays','createdate','startdate','returndate','motif','creator','status']
