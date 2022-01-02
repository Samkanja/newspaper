from django.urls import path
from .views import SignUpview
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', SignUpview.as_view(), name='signup'),
]