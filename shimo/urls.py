from django.urls import path
from  shimo import views
from .views import *

urlpatterns = [
    path('',ListYato.as_view())
]