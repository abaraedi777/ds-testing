from django.urls import path
from . import views

app_name = "sales"

urlpatterns = [
    path("", views.SalesView.as_view(), name="sales_view")
]
