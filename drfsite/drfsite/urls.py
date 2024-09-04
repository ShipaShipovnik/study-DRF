from django.urls import path
from django.contrib import admin
from women.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/womenlist/', WomenAPIList.as_view()),
]