from django.urls import path
from . import views

urlpatterns = [
    path('category/' , views.category),
    path("product/" , views.product),
    path('motherboard/' , views.motherboard),
    path("computer_case/" , views.computer_case),
    path('graphics_card/' , views.graphics_card),
    path('processor/' , views.processor),
    path('case_fan/' , views.case_fan),
    path('keyboard/' , views.keyboard),
    path('monitor/' , views.monitor),
    path('mouse/' , views.mouse),
    path('ram/' , views.ram),    
    path('cooler/' , views.cooler),
  
]

