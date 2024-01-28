from django.shortcuts import render
from django.views import View
from .models import Sale

# Create your views here.

class SalesView(View):
    def get(self, request, *args, **kwargs):
        all_sale = Sale.objects.all()
        context = {
            "all_sale":all_sale
        }
        return render(request, "sales/sales.html", context)