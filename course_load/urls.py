from django.urls import path

from course_load.views import (views)

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view()),
    path('get-data/', views.get_data),
    path('submit-data/', views.submit_data),
    path('download-course-wise', views.download_course_wise),
    path('download-instructor-wise', views.download_instructor_wise),
]
