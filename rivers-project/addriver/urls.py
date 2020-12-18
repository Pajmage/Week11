from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.New_River, name='river-home'),
    path('results/', views.View_River_Details, name='results'),
]
