from django.urls import path
from remotework import views

urlpatterns = [
    path('add-remotework/',views.CreateRemotework.as_view(),name='add-Remotework'),
    path('list-remotework/',views.ListRemotework.as_view(),name='list-Remotework'),
    path('delete-remotework/<int:id>',views.updateDestroyRemoteworkApiView.as_view(),name='delete-Remotework'),
    path('update-remotework/<int:id>',views.updateDestroyRemoteworkApiView.as_view(),name='update-Remotework'),
    path('getremotework/<int:id>',views.getRemoteworkApiView.as_view(),name='get-Remotework'),
    path('listremotework/',views.ListallRemotework.as_view(),name='listallRemotework'),
    # path('GetRemoteworkByUser/<int:id>',views.GetRemoteworkByUser.as_view(),name='GetRemoteworkByUser'),
    # path('GetRemoteworkByCreator/<int:id>',views.GetRemoteworkByCreator.as_view(),name='GetRemoteworkByCreator'),

    path('add-remoteworkplan/',views.CreateRemoteworkplan.as_view(),name='add-remoteworkplan'),
    path('list-remoteworkplan/',views.ListRemoteworkplan.as_view(),name='list-remoteworkplan'),
    path('delete-remoteworkplan/<int:id>',views.updateDestroyRemoteworkplanApiView.as_view(),name='delete-remoteworkplan'),
    path('update-remoteworkplan/<int:id>',views.updateDestroyRemoteworkplanApiView.as_view(),name='update-remoteworkplan'),
    path('getremoteworkplan/<int:id>',views.getRemoteworkplanApiView.as_view(),name='get-remoteworkplan'),
    path('listremoteworkplan/',views.ListallRemoteworkplan.as_view(),name='listallremoteworkplan'),
    # path('GetRemoteworkplanByUser/<int:id>',views.GetRemoteworkplanByUser.as_view(),name='GetRemoteworkplanByUser'),
    # path('GetRemoteworkplanByCreator/<int:id>',views.GetRemoteworkplanByCreator.as_view(),name='GetRemoteworkplanByCreator'),
]