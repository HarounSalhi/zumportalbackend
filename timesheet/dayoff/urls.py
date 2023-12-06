from django.urls import path
from dayoff import views

urlpatterns = [
    path('add-dayoff/',views.CreateDayoff.as_view(),name='add-dayoff'),
    path('list-dayoff/',views.ListDayoff.as_view(),name='list-dayoff'),
    # path('update-dayoff/<int:id>/',views.UpdateDayoff.as_view(),name='update-dayoff'),
    path('delete-dayoff/<int:id>',views.updateDestroyDayoffApiView.as_view(),name='delete-dayoff'),
    path('update-dayoff/<int:id>',views.updateDestroyDayoffApiView.as_view(),name='update-dayoff'),
    
    path('approuve-dayoff/<int:id>',views.approuveDayoffApiView.as_view(),name='approuve-dayoff'),
    path('decline-dayoff/<int:id>',views.declineDayoffApiView.as_view(),name='decline-dayoff'),

    path('get-dayoff/<int:id>',views.getDayoffApiView.as_view(),name='get-dayoff'),
    path('list-dayoff/',views.ListallDayoff.as_view(),name='listalldayoff'),
    # path('GetDayoffByUser/<int:id>',views.GetDayoffByUser.as_view(),name='GetDayoffByUser'),
    # path('GetDayoffByCreator/<int:id>',views.GetDayoffByCreator.as_view(),name='GetDayoffByCreator'),
    # path('GetDayoffByCreatorWithaffectedTo/<int:id>',views.GetDayoffByCreatorWithaffectedTo.as_view(),name='GetDayoffByCreatorWithaffectedTo'),

    
]