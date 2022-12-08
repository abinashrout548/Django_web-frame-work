from django.urls import path
from myapp import views

urlpatterns = [
    path('dt', views.date_time),
    path('v2', views.v2),
    path(' ', views.home),
    path('math', views.math),
]
