"""timesheet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('project/', include('project.urls')),
    path('task/', include('task.urls')),
    path('dayoff/', include('dayoff.urls')),
    path('equipment/', include('equipment.urls')),
    path('meetingroom/', include('meetingroom.urls')),
    path('rm/', include('rooms.urls')),
    path('remotework/', include('remotework.urls')),
  # path('mongo_auth/', include('mongo_auth.urls')),
    path('api_auth/', include('rest_framework.urls')),

]
