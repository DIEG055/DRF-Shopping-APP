from shopping.models import Customer, Order, Product
from shopping.serializers import CustomerSerializer, OrderSerializer, ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import viewsets


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'customers': reverse('customers-list', request=request, format=format),
        'orders': reverse('orders-list', request=request, format=format),
        'products': reverse('products-list', request=request, format=format)
    })


class CustomerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
