from . import views
from django.urls import path

urlpatterns = [
    path('', views.Calendar_view.as_view(), name='home'),
]