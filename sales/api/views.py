from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from sales.models import Sale

from sales.api.serializers import SaleSerializer


@api_view(['GET'])
def sale_list_api_view(request):
    sales = Sale.objects.all()
    serializer = SaleSerializer(sales, many=True)
    return Response(serializer.data)