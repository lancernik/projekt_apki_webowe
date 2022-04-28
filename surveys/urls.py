from django.urls import path, include

from surveys.views import *

urlpatterns = [
    path(r'add_drug/', AddDrugView.as_view(), name='add_drug'),
    path(r'filled_success/', SurveyFilledView.as_view(), name='filled_success'),
    path(r'drugs_stats/', CurrentDragsStatsView.as_view(), name='drugs_stats'),
]
