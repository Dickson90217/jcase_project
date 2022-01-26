from django.contrib import admin
from django .urls import Path
from . import views


urlpatterns = [
    path('',views.cases(name='cases'))
]