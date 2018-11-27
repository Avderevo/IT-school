from django.urls import path
from .views import (
    ConfirmView, UserCreate, LogView, RemindPasswordView,
    RestorePasswordConfirmView, LogoutView)

app_name = 'users'

urlpatterns = [
    path('confirm/<code>/', ConfirmView.as_view(), name='confirm'),
    path('create/', UserCreate.as_view(), name='create'),
    path('login/', LogView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('remind/', RemindPasswordView.as_view(), name='remind'),
    path('restore/<uidb64>/<token>/', RestorePasswordConfirmView.as_view(),
        name='restore_password'),
]