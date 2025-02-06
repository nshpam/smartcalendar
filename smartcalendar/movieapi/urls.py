from django.urls import path
from . import views

app_name = "movieapi"

urlpatterns = [
    path("", views.index, name= "index" )
]