from django.urls import path
from meetingroom import views

urlpatterns = [
    path('add-meetingroom/',views.CreateMeetingroom.as_view(),name='add-meetingroom'),
    path('list-meetingroom/',views.ListMeetingroom.as_view(),name='list-meetingroom'),
    # path('update-meetingroom/<int:id>/',views.Updatemeetingroom.as_view(),name='update-meetingroom'),
    path('delete-meetingroom/<int:id>',views.updateDestroyMeetingroomApiView.as_view(),name='delete-meetingroom'),
    path('update-meetingroom/<int:id>',views.updateDestroyMeetingroomApiView.as_view(),name='update-meetingroom'),
    path('getmeetingroom/<int:id>',views.getMeetingroomApiView.as_view(),name='get-meetingroom'),
    path('listmeetingroom/',views.ListallMeetingroom.as_view(),name='listallmeetingroom'),
    # path('GetmeetingroomByUser/<int:id>',views.GetmeetingroomByUser.as_view(),name='GetmeetingroomByUser'),
    # path('GetmeetingroomByCreator/<int:id>',views.GetmeetingroomByCreator.as_view(),name='GetmeetingroomByCreator'),
    # path('GetmeetingroomByCreatorWithaffectedTo/<int:id>',views.GetmeetingroomByCreatorWithaffectedTo.as_view(),name='GetmeetingroomByCreatorWithaffectedTo'),

    
]