from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('', lambda request: redirect('course-load/dashboard', permanent=False)),
    path('admin/', admin.site.urls),
    path('course-load/', include('course_load.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]