from django.urls import path
from authentication import views
from rest_framework_simplejwt.views import TokenRefreshView



urlpatterns=[
    path('login/',views.LoginAPIView.as_view(),name="login"),
    path('logout/',views.LogoutAPIView.as_view(),name="logout"),
    path('user/',views.AuthUserAPIView.as_view(),name="auth-user"),
    path('listuser/',views.GetAllUsers.as_view(),name="list-user"),
    path('list-user/', views.GetAllUser.as_view(), name='list-user'),
    path('register-user/',views.RegisterUserViaEmail.as_view(),name='register-user'),
    path('updateafterregister/<int:id>', views.UpdateAfterRegister.as_view(), name='UpdateAfterRegister'),
    path('resetpassword/', views.ResetPasswordViaEmailView.as_view(), name='ResetPasswordViaEmail'),
    path('updateUser/<str:id>',views.updateDestroyUserApiView.as_view(),name='updateuser'),
    path('deleteUser/<str:id>',views.updateDestroyUserApiView.as_view(),name='deleteuser'),
    path('updateUserPhoto/<str:id>', views.UserProfilePhotoUploadView.as_view(), name='upload-profile-photo'),

]