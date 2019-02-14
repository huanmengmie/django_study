# -*- coding: utf-8 -*-
from django.urls import path

from polls import views

urlpatterns = [
    path("", views.index, name="index"),
]
