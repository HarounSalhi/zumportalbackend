from rest_framework import permissions
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView
from .models import Dayoff
from .serializers import ApprouveDayoffSerilaizer, DayoffSerilaizer, DeclineDayoffSerilaizer,GetDayoffSerilaizer,UpdateDayoffSerilaizer,GetAllDayoffSerilaizer
# Create your views here.
class CreateDayoff(CreateAPIView):
    authentication_classes=[]
    serializer_class = DayoffSerilaizer
    queryset = Dayoff.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        return serializer.save()

class ListDayoff(ListAPIView):
    authentication_classes=[]
    serializer_class = GetDayoffSerilaizer
    queryset = Dayoff.objects.all()
    def get_queryset(self):
        return self.queryset.all()

class updateDestroyDayoffApiView(RetrieveUpdateDestroyAPIView):
    authentication_classes=[]
    queryset=Dayoff.objects.all()
    serializer_class = UpdateDayoffSerilaizer
    lookup_field="id"
    def get_queryset(self):
        return self.queryset
    
class approuveDayoffApiView(RetrieveUpdateDestroyAPIView):
    authentication_classes=[]
    queryset=Dayoff.objects.all()
    serializer_class = ApprouveDayoffSerilaizer
    lookup_field="id"
    def get_queryset(self):
        return self.queryset
    
class declineDayoffApiView(RetrieveUpdateDestroyAPIView):
    authentication_classes=[]
    queryset=Dayoff.objects.all()
    serializer_class = DeclineDayoffSerilaizer
    lookup_field="id"
    def get_queryset(self):
        return self.queryset

class getDayoffApiView(RetrieveUpdateDestroyAPIView):
    authentication_classes=[]
    queryset=Dayoff.objects.all()
    serializer_class = GetDayoffSerilaizer
    lookup_field="id"
    def get_queryset(self):
        return self.queryset



class ListallDayoff(ListAPIView):
    authentication_classes=[]
    serializer_class = GetAllDayoffSerilaizer
    queryset = Dayoff.objects.all()
    def get_queryset(self):
        return self.queryset.all()
        
# class GetDayoffByUser(ListAPIView):
#     authentication_classes=[]
#     serializer_class = GetDayoffByUserSerilaizer
#     def get_queryset(self):
#         return Dayoff.objects.values().filter(assigned_to = self.kwargs['id'])



# class GetDayoffByCreator(ListAPIView):
#     authentication_classes=[]
#     serializer_class = GetDayoffBycreatorSerilaizer
#     def get_queryset(self):
#         return Dayoff.objects.values().filter(created_by = self.kwargs['id'])



# class GetDayoffByCreatorWithaffectedTo(ListAPIView):
#     authentication_classes=[]
#     serializer_class = GetDayoffBycreatorWithAffectedToSerilaizer
    
#     def get_queryset(self):
#         q = Dayoff.objects.values().filter(created_by = self.kwargs['id'])
#         t=q['assigned_to']      
#         return q       


# class DayoffViewSet(viewsets.ModelViewSet):
#     authentication_classes = []
#     queryset = Dayoff.objects.all()
#     serializer_class = DayoffSerilaizer

#     def perform_create(self, serializer):
#         serializer.save()

#     def get_queryset(self):
#         return self.queryset.all()

#     # @action(detail=True, methods=['post'])
#     def approve(self, request, pk=None):
#         dayoff = self.get_object()
#         dayoff_serializer = DayoffSerilaizer(dayoff, data=request.data, partial=True)

#         if dayoff_serializer.is_valid():
#             dayoff_serializer.save(status='Approved')
#         #     return Response({'message': 'Dayoff approved'}, status=status.HTTP_200_OK)
#         # else:
#         #     return Response(dayoff_serializer.errors, status=status.HTTP_400_BAD_REQUEST)