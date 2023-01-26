from . import views
from django.urls import path

urlpatterns = [
    path('', views.main, name='home'),
    path('details/', views.Calendar_view.as_view(), name='details'),
]