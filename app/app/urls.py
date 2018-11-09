from django.urls import path, include
from django.contrib import admin
from school.views import IndexPageView
from django.conf import settings

if settings.DEBUG:
    import debug_toolbar


urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('django-rq/', include('django_rq.urls')),
    path('', IndexPageView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('school/', include('school.urls')),
]
