from django.urls import path
from myapp1 import views

urlpatterns = [
    path('f1/', views.f1),
    path('f2/', views.f2),

]
