from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from course_load.views import (views)

urlpatterns = [
    path('', lambda request: redirect('course-load/dashboard', permanent=False)),
    path('admin/', admin.site.urls),
    path('course-load/', include('course_load.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('add-course/', views.AddCourse.as_view()),
    path('add-instructor/', views.AddInstructor.as_view()),
    path('update-course/', views.UpdateCourse.as_view()),
    path('update-instructor/', views.UpdateInstructor.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)