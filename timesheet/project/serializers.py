from requests import Response
from rest_framework import serializers
from .models import Project
from authentication.serializers import Registerserilaizer,UserAssginedToProjectSerializer,userSerializer
from .models import User

class ProjectSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name','description','starter_at','created_by','scrum_master','assigned_to','end_date','id',]

class GetProjectSerilaizer(serializers.ModelSerializer):
    created_by = userSerializer(required = True)
    assigned_to = userSerializer(many=True)
    class Meta:
        model = Project
        fields = ['name','description','status','starter_at','created_by','scrum_master','assigned_to','end_date','id',]
        depth = 1



class GetAllProjectSerilaizer(serializers.ModelSerializer):
    assigned_to = userSerializer(many=True)
    created_by = userSerializer(required = True)

    class Meta:
        model = Project
        fields = ['id','name','description','status','starter_at','created_by','scrum_master','assigned_to','end_date',]

        
class UpdateProjectSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id','name','description','status','starter_at','created_by','scrum_master','assigned_to','end_date',)
        def update(self, instance, validated_data):
            instance.name = validated_data.pop('name', instance.name)
            instance.description = validated_data.pop('descreption', instance.description)
            instance.status = validated_data.pop('status', instance.status)
            instance.assigned_to = validated_data.pop('assigned_to', instance.assigned_to)
            instance.scrum_master = validated_data.pop('scrum_master', instance.scrum_master)
            if instance.status == 'active':
                try:
                    user = User.objects.get(id=instance.scrum_master.id)
                    user.role("SM")
                    user.save()
                except User.DoesNotExist:
                    return Response({'detail': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)
            else:
                try:
                    user = User.objects.get(id=instance.scrum_master.id)
                    user.role("SM")
                    user.save()
                except User.DoesNotExist:
                    return Response({'detail': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)

            instance.save()
            return instance


class GetProjectByUserSerilaizer(serializers.ModelSerializer):
    created_by_id = Registerserilaizer
    class Meta:
        model = Project
        fields = ['id','name','starter_at','description','status','end_date','created_by_id',]


class GetProjectBycreatorSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id','name','starter_at','description','status','end_date',]    

   

class GetProjectBycreatorWithAffectedToSerilaizer(serializers.ModelSerializer):
    # assigned_to = Registerserilaizer
    assigned_to = UserAssginedToProjectSerializer(many=True)
    class Meta:
        model = Project
        fields = ['id','name','starter_at','description','status','end_date','assigned_to',]    

# class GetProjectBycreatorSerilaizer(serializers.ModelSerializer):
#     # assigned_to = Registerserilaizer
#     assigned_to = UserAssginedToProjectSerializer(many=True)
#     class Meta:
#         model = Project
#         fields = ['id','name','starter_at','description','status','end_date','assigned_to',]    
#         depth=1        

#     def get_assigned_to(self,obj):
#         if not hasattr(obj,'name'):
#             return None
#         if not isinstance(obj,Project):
#             return None
#         return  Project.objects.get(assigned_to=obj['assigned_to'])  

  