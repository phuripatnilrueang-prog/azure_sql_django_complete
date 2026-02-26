from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.urls import path
from . import views

from api.views import api_root

def favicon(request):
    return HttpResponse(status=204)

urlpatterns = [
    path('favicon.ico', favicon),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', api_root),
    path('users/',        views.UserList.as_view(),     name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('users/deleteAll/', views.UserDeleteAll.as_view(), name='user_delete_all'),
]
