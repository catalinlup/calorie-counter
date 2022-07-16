from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('nutri_value/<slug:id>/', views.nutri_value, name="nutri_value")
]