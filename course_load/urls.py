from django.urls import path
from django.conf.urls import url

from course_load.views import (views)

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view()),
    path('get-data/', views.get_data),
]
