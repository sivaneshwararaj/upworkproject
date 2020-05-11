from django.contrib import admin
from django.urls import path,include
from .views import BodyView

urlpatterns = [
  
    path('',BodyView.as_view())

]
