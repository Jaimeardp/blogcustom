from core.views import HomeView, SampleView
from django.urls import path
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('sample/', SampleView.as_view(), name="sample"),
]