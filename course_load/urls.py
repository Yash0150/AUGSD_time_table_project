from django.urls import path

from course_load.views import (views)

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view()),
    path('get-data/', views.get_data),
]
