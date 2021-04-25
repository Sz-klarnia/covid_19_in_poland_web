from django.urls import path
from . import views

# urls of chart pages
urlpatterns = [
    path('regional_case_map/',views.cases,name="case_map"),  # cases subpage
    path('regional_tests_map/',views.testing,name="test_map"), # tests subpage
    path('regional_hosp_map/',views.hospitals,name="hosp_map"), # hospitalizations subpage
    path('regional_region-<str:region_id>/',views.region,name="region"), #regional pages
]