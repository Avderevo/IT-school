from django.urls import path, include
from django.contrib import admin
from school.views import IndexPageView


urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('school/', include('school.urls')),
    path('django-rq/', include('django_rq.urls')),
]
