"""covid_19 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls), # admin urls
    path('', include('pages.urls')), # static page urls
    path('pl/',include("chart_page.urls")), # chart pages urls
    path('',include('regional.urls')), # regional pages urls
    path('predictions/',include('predictions.urls')) # predictions page url
] 

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)