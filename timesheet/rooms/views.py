from django.shortcuts import render
from rest_framework.response import Response
from rooms.serializers import RoomSerializer
from rest_framework.views import APIView
from rooms.models import Room ,Equipement, RequestRooms
from rest_framework.decorators import api_view 
from rooms.serializers import RoomSerializer
from rooms.serializers import EquipementSerializer
from rooms.serializers import RequestRoomsSerializer
from datetime import datetime, time



# Create your views here.


class RoomAPI(APIView):
    authentication_classes = []

    def get(self, request):
        objs = Room.objects.all()
        serializer = RoomSerializer(objs, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = RoomSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self, request):
        data = request.data
        obj = Room.objects.get(id=data['id'])

        if request.method == 'PATCH':
            data['dispo'] = 1
        serializer = RoomSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request):
        data = request.data
        obj = Room.objects.get(id=data['id'])
        obj.delete()
        return Response({'message': 'Room deleted'})

class EquipAPI(APIView):
    authentication_classes = []

    def get(self, request):
        objs = Equipement.objects.all()
        serializer = EquipementSerializer(objs, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = EquipementSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self, request):
        data = request.data
        obj = Equipement.objects.get(id=data['id'])
        serializer = EquipementSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request):
        data = request.data
        obj = Equipement.objects.get(id=data['id'])
        obj.delete()
        return Response({'message': 'Equipement deleted'})

class RequestRoomsAPI(APIView):
    authentication_classes = []
    
    
    def get(self, request):
        objs = RequestRooms.objects.all()
        serializer = RequestRoomsSerializer(objs, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        data = request.data
        serializer = RequestRoomsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    # def patch(self, request):
    #     data = request.data
    #     obj = RequestRooms.objects.get(id=data['id'])
    #     serializer = RequestRoomsSerializer(obj, data=data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)

    def patch(self, request):
        data = request.data
        obj = RequestRooms.objects.get(id=data['id'])

    # Mettre à jour l'attribut 'etat' à 0 si la méthode PATCH est choisie
        if request.method == 'PATCH':
            data['etat'] = 0

        serializer = RequestRoomsSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



    def delete(self, request):
        data = request.data
        obj = RequestRooms.objects.get(id=data['id'])
        obj.delete()
        return Response({'message': 'RequestRooms deleted'})


    # def delete(self, request, pk):
    #     try:
    #         obj = RequestRooms.objects.get(id=pk)
    #         obj.delete()
    #         return Response({'message': 'RequestRooms deleted'}, status=status.HTTP_204_NO_CONTENT)
    #     except RequestRooms.DoesNotExist:
    #         return Response({'message': 'RequestRooms not found'}, status=status.HTTP_404_NOT_FOUND)


class RoomAPI2(APIView):
    authentication_classes = []

    def get(self, request):
        objs = Room.objects.all()
        serializer = RoomSerializer(objs, many=True)
        return Response(serializer.data)
        
    def patch(self, request):
        data = request.data
        obj = Room.objects.get(id=data['id'])

        if request.method == 'PATCH':
            data['dispo'] = 0
        serializer = RoomSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)