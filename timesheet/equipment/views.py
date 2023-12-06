from rest_framework import permissions
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView
from .models import Equipment
from .serializers import EquipmentSerilaizer,GetEquipmentSerilaizer,UpdateEquipmentSerilaizer,GetAllEquipmentSerilaizer
# Create your views here.
class CreateEquipment(CreateAPIView):
    authentication_classes=[]
    serializer_class = EquipmentSerilaizer
    queryset = Equipment.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        return serializer.save()

class ListEquipment(ListAPIView):
    authentication_classes=[]
    serializer_class = GetEquipmentSerilaizer
    queryset = Equipment.objects.all()
    def get_queryset(self):
        return self.queryset.all()

class updateDestroyEquipmentApiView(RetrieveUpdateDestroyAPIView):
    authentication_classes=[]
    queryset=Equipment.objects.all()
    serializer_class = UpdateEquipmentSerilaizer
    lookup_field="id"
    def get_queryset(self):
        return self.queryset
        # for nesrine
class getEquipmentApiView(RetrieveUpdateDestroyAPIView):
    authentication_classes=[]
    queryset=Equipment.objects.all()
    serializer_class = GetEquipmentSerilaizer
    lookup_field="id"
    def get_queryset(self):
        return self.queryset



class ListallEquipment(ListAPIView):
    authentication_classes=[]
    serializer_class = GetAllEquipmentSerilaizer
    queryset = Equipment.objects.all()
    def get_queryset(self):
        return self.queryset.all()
        
# class GetEquipmentByUser(ListAPIView):
#     authentication_classes=[]
#     serializer_class = GetEquipmentByUserSerilaizer
#     def get_queryset(self):
#         return Equipment.objects.values().filter(assigned_to = self.kwargs['id'])



# class GetEquipmentByCreator(ListAPIView):
#     authentication_classes=[]
#     serializer_class = GetEquipmentBycreatorSerilaizer
#     def get_queryset(self):
#         return Equipment.objects.values().filter(created_by = self.kwargs['id'])



# class GetEquipmentByCreatorWithaffectedTo(ListAPIView):
#     authentication_classes=[]
#     serializer_class = GetEquipmentBycreatorWithAffectedToSerilaizer
    
#     def get_queryset(self):
#         q = Equipment.objects.values().filter(created_by = self.kwargs['id'])
#         t=q['assigned_to']      
#         return q       