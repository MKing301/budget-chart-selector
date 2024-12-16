from django.urls import path
from . import views

urlpatterns = [
    path('', views.budget_chart, name='budget_chart'),
]
