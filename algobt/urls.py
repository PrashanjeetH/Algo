from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from algobt import views

urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

    path('conditionform/', views.conditionForm, name='ConditionForm'),
    path('showrecords/', views.ShowDataRecords, name='ShowRecords'),
    # path('downloadrecords/<int:record_id>', views.DownloadDataRecords, name='DownloadRecords'),
    path('accounts/signup/', views.restricted_404_view, name='404view'),
    path('download/<int:record_id>', views.DownloadDataRecords, name='DownloadRecords'),
 ]
