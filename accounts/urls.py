from django.contrib import admin
from accounts.views import SignupView
from django.urls import path, include

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', SignupView.as_view(), name='signup')
]