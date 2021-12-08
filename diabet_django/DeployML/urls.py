
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from DjangoAPI import views

urlpatterns = [
    url(f'^Diabet_Prediction', views.DjangoAPIView.as_view()),
]

