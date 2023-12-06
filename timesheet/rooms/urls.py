from django.urls import path 
from rooms.views import RoomAPI , EquipAPI ,RequestRoomsAPI , RoomAPI2



urlpatterns = [
    path('rooms/' , RoomAPI.as_view()) ,
    path('equip/' , EquipAPI.as_view()) ,
    path('equipAjout/', EquipAPI.as_view(), name='equip-post'),
    path('requestrooms/' , RequestRoomsAPI.as_view()) ,
    path('rooms2/' , RoomAPI2.as_view()) ,
]





