from rest_framework import permissions
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView
from .models import Remotework
from .models import Remoteworkplan
from .serializers import RemoteworkSerilaizer,GetRemoteworkSerilaizer,UpdateRemoteworkSerilaizer,GetAllRemoteworkSerilaizer
from .serializers import RemoteworkplanSerilaizer,GetRemoteworkplanSerilaizer,UpdateRemoteworkplanSerilaizer,GetAllRemoteworkplanSerilaizer
# Create your views here.
class CreateRemotework(CreateAPIView):
    authentication_classes=[]
    serializer_class = RemoteworkSerilaizer
    queryset = Remotework.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        return serializer.save()

class ListRemotework(ListAPIView):
    authentication_classes=[]
    serializer_class = GetRemoteworkSerilaizer
    queryset = Remotework.objects.all()
    def get_queryset(self):
        return self.queryset.all()

class updateDestroyRemoteworkApiView(RetrieveUpdateDestroyAPIView):
    authentication_classes=[]
    queryset=Remotework.objects.all()
    serializer_class = UpdateRemoteworkSerilaizer
    lookup_field="id"
    def get_queryset(self):
        return self.queryset
        # for nesrine
class getRemoteworkApiView(RetrieveUpdateDestroyAPIView):
    authentication_classes=[]
    queryset=Remotework.objects.all()
    serializer_class = GetRemoteworkSerilaizer
    lookup_field="id"
    def get_queryset(self):
        return self.queryset



class ListallRemotework(ListAPIView):
    authentication_classes=[]
    serializer_class = GetAllRemoteworkSerilaizer
    queryset = Remotework.objects.all()
    def get_queryset(self):
        return self.queryset.all()
        
# class GetRemoteworkByUser(ListAPIView):
#     authentication_classes=[]
#     serializer_class = GetRemoteworkByUserSerilaizer
#     def get_queryset(self):
#         return Remotework.objects.values().filter(assigned_to = self.kwargs['id'])



# class GetRemoteworkByCreator(ListAPIView):
#     authentication_classes=[]
#     serializer_class = GetRemoteworkBycreatorSerilaizer
#     def get_queryset(self):
#         return Remotework.objects.values().filter(created_by = self.kwargs['id'])



# class GetRemoteworkByCreatorWithaffectedTo(ListAPIView):
#     authentication_classes=[]
#     serializer_class = GetRemoteworkBycreatorWithAffectedToSerilaizer
    
    def get_queryset(self):
        q = Remotework.objects.values().filter(created_by = self.kwargs['id'])
        t=q['assigned_to']      
        return q       

class CreateRemoteworkplan(CreateAPIView):
    authentication_classes=[]
    serializer_class = RemoteworkplanSerilaizer
    queryset = Remoteworkplan.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        return serializer.save()

class ListRemoteworkplan(ListAPIView):
    authentication_classes=[]
    serializer_class = GetRemoteworkplanSerilaizer
    queryset = Remoteworkplan.objects.all()
    def get_queryset(self):
        return self.queryset.all()

class updateDestroyRemoteworkplanApiView(RetrieveUpdateDestroyAPIView):
    authentication_classes=[]
    queryset=Remoteworkplan.objects.all()
    serializer_class = UpdateRemoteworkplanSerilaizer
    lookup_field="id"
    def get_queryset(self):
        return self.queryset
        # for nesrine
class getRemoteworkplanApiView(RetrieveUpdateDestroyAPIView):
    authentication_classes=[]
    queryset=Remoteworkplan.objects.all()
    serializer_class = GetRemoteworkplanSerilaizer
    lookup_field="id"
    def get_queryset(self):
        return self.queryset



class ListallRemoteworkplan(ListAPIView):
    authentication_classes=[]
    serializer_class = GetAllRemoteworkplanSerilaizer
    queryset = Remoteworkplan.objects.all()
    def get_queryset(self):
        return self.queryset.all()
        
# class GetRemoteworkplanByUser(ListAPIView):
#     authentication_classes=[]
#     serializer_class = GetRemoteworkplanByUserSerilaizer
#     def get_queryset(self):
#         return Remoteworkplan.objects.values().filter(assigned_to = self.kwargs['id'])



# class GetRemoteworkplanByCreator(ListAPIView):
#     authentication_classes=[]
#     serializer_class = GetRemoteworkplanBycreatorSerilaizer
#     def get_queryset(self):
#         return Remoteworkplan.objects.values().filter(created_by = self.kwargs['id'])



# class GetRemoteworkplanByCreatorWithaffectedTo(ListAPIView):
#     authentication_classes=[]
#     serializer_class = GetRemoteworkplanBycreatorWithAffectedToSerilaizer
    
#     def get_queryset(self):
#         q = Remoteworkplan.objects.values().filter(created_by = self.kwargs['id'])
#         t=q['assigned_to']      
#         return q       