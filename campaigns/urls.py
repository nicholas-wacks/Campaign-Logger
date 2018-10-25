from django.urls import path
from campaigns import views


urlpatterns = [
    path('', views.index, name='index'),
]