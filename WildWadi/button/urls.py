from django.urls import path
from . import views

urlpatterns = [
    path('', views.button_home, name="button_home"),
    # path('button/total_price/', views.total_price, name="total_price"),


]