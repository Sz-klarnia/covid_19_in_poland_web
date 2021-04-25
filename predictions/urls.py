from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('',predictions,name="predictions"),
    path('model_info',model_info,name="model_info")
]