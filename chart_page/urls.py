from django.urls import path
from . import views

# urls of chart pages
urlpatterns = [
    path('cases',views.cases,name='cases'), # cases subpage 
    path('hospitals',views.hospitals,name='hospitals'), # hospitalizations subpage
    path('testing',views.testing,name="testing"), # testing subpage
    path('vacc',views.vacc,name="vacc") # vaccinations subpage
]
