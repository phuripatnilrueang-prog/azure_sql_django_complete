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
]
