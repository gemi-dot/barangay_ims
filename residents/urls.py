from django.urls import path
from . import views

app_name = 'residents'

urlpatterns = [
    # Add resident-specific URLs here as needed
    path('reports/', views.reports_home, name='reports_home'),
    path('voters-report/', views.voters_report, name='voters_report'),
    path('voters-by-precinct/', views.voters_by_precinct_report, name='voters_by_precinct'),
    path('dashboard/voters-by-precinct/', views.voters_precinct_dashboard, name='voters_precinct_dashboard'),

    
]