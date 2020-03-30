from django.urls import path
from django.views.generic import TemplateView
from course_load.views import (views)
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # path('dashboard/', login_required(TemplateView.as_view(template_name='index.html'))),
    path('dashboard/', views.DashboardView.as_view()),
    path('get-data/', views.get_data),
    path('get-course-data/', views.get_course_data),
    path('submit-data/', views.submit_data),
    path('add-comment/', views.AddComment.as_view()),
    path('request-course-access/', views.request_course_access),
    path('download-course-wise/', views.download_course_wise),
    path('download-instructor-wise/', views.download_instructor_wise),
]