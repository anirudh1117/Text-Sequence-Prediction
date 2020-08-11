from django.urls import path

from .import views

urlpatterns = [
    path('',views.viewDataset,name='Dataset')
    ]