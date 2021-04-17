from django.urls import path
from . import views

# urls of chart pages
urlpatterns = [
    path('',views.regions,name='regions'), # main page of regions
    path('case_map/',views.cases,name="case_map"),  # cases subpage
    path('tests_map/',views.testing,name="test_map"), # tests subpage
    path('hosp_map/',views.hospitals,name="hosp_map"), # hospitalizations subpage
    path('region-<str:region_id>/',views.region,name="region"), #regional pages
]