from django.contrib import admin
from django.urls import path
from student.views  import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('studentadd/', StudentAddView.as_view(), name='studentadd'),
    path('studentprint/', StudenPrintView.as_view(), name='studentprint'),
    path('studentmigration/', StudenMigrations.as_view(), name='studentmigration'),
]
