from django.contrib import admin
from django .urls import Path
from . import views


urlpatterns = [
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_login,name='logout')
]