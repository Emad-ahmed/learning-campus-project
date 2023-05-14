from django.contrib import admin
from django.urls import path
from student.views  import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('studentadd/', StudentAddView.as_view(), name='studentadd'),
]
