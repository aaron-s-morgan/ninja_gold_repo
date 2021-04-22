from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('process_gold_farm', views.process_gold_farm),
    path('process_gold_cave', views.process_gold_cave),
    path('process_gold_house', views.process_gold_house),
    path('process_gold_casino', views.process_gold_casino),
    path('reset', views.reset),
]