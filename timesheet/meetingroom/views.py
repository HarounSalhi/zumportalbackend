from rest_framework import permissions
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView
from .models import Meetingroom
from .serializers import MeetingroomSerilaizer,GetMeetingroomSerilaizer,UpdateMeetingroomSerilaizer,GetAllMeetingroomSerilaizer
# Create your views here.
class CreateMeetingroom(CreateAPIView):
    authentication_classes=[]
    serializer_class = MeetingroomSerilaizer
    queryset = Meetingroom.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        return serializer.save()

class ListMeetingroom(ListAPIView):
    authentication_classes=[]
    serializer_class = GetMeetingroomSerilaizer
    queryset = Meetingroom.objects.all()
    def get_queryset(self):
        return self.queryset.all()

class updateDestroyMeetingroomApiView(RetrieveUpdateDestroyAPIView):
    authentication_classes=[]
    queryset=Meetingroom.objects.all()
    serializer_class = UpdateMeetingroomSerilaizer
    lookup_field="id"
    def get_queryset(self):
        return self.queryset
        # for nesrine
class getMeetingroomApiView(RetrieveUpdateDestroyAPIView):
    authentication_classes=[]
    queryset=Meetingroom.objects.all()
    serializer_class = GetMeetingroomSerilaizer
    lookup_field="id"
    def get_queryset(self):
        return self.queryset



class ListallMeetingroom(ListAPIView):
    authentication_classes=[]
    serializer_class = GetAllMeetingroomSerilaizer
    queryset = Meetingroom.objects.all()
    def get_queryset(self):
        return self.queryset.all()
        
# class GetMeetingroomByUser(ListAPIView):
#     authentication_classes=[]
#     serializer_class = GetMeetingroomByUserSerilaizer
#     def get_queryset(self):
#         return Meetingroom.objects.values().filter(assigned_to = self.kwargs['id'])



# class GetMeetingroomByCreator(ListAPIView):
#     authentication_classes=[]
#     serializer_class = GetMeetingroomBycreatorSerilaizer
#     def get_queryset(self):
#         return Meetingroom.objects.values().filter(created_by = self.kwargs['id'])



# class GetMeetingroomByCreatorWithaffectedTo(ListAPIView):
#     authentication_classes=[]
#     serializer_class = GetMeetingroomBycreatorWithAffectedToSerilaizer
    
#     def get_queryset(self):
#         q = Meetingroom.objects.values().filter(created_by = self.kwargs['id'])
#         t=q['assigned_to']      
#         return q       