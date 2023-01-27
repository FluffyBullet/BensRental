from . import views
from django.urls import path

urlpatterns = [
    path('', views.main, name='home'),
    path('details/', views.Customer_feedback.as_view(), name='details'),
    path('availability/', views.Calendar_view.as_view(), name='check_avail'),
]