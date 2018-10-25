from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import SignUpView, ConfirmView, IndexView, UserCreate, LogView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('thanks/', views.thanks, name='thanks'),
    path('confirm/<code>/', ConfirmView.as_view(), name='confirm'),
    path('index/', IndexView.as_view(), name='index'),
    path('index/create/', UserCreate.as_view(), name='create'),
    path('index/login/', LogView.as_view(), name='login'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
