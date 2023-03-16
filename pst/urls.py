from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('view posts/',views.view_posts),
]