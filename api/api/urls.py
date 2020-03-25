"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from rest.views import UserModelViewSet, GroupModelViewSet, PermissionModelViewSet
from rest_framework.routers import DefaultRouter

restRouter = DefaultRouter()
restRouter.register(r'users', UserModelViewSet)
restRouter.register(r'groups', GroupModelViewSet)
restRouter.register(r'permissions', PermissionModelViewSet)

# Wire up API
urlpatterns = [
    path('', include(restRouter.urls)),
    # from rest framework API authorization
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
