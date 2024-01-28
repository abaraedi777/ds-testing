from django.urls import path
from .views import sale_list_api_view

urlpatterns = [
    path('', sale_list_api_view, name='sale-list'),
]