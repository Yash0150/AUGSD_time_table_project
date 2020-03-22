from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('course-load/', include('course_load.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]