from django.urls import path
from . import views


# URLs of static pages
urlpatterns = [
    path('', views.index, name='index'),
]
