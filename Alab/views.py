from django.db.models import Sum
from rest_framework import generics, viewsets
from rest_framework.response import Response
from .serializer import ProductSerializer, ProductCount
from .models import Product


# Create your views here.


class ProductApi(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer_data = self.get_serializer(queryset, many=True).data
        for indx in range(len(serializer_data)):
            serializer_data[indx].update(
                {'total_price': list(serializer_data[indx].values())[2] * list(serializer_data[indx].values())[4]})
        return Response(serializer_data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance).data
        serializer['total_price'] = serializer['quantity'] * serializer['price']
        return Response(serializer)


class ProductCount(generics.GenericAPIView):
    queryset = Product.objects.aggregate(total_price=Sum('price'))
    serializer_class = ProductCount

    def get(self, request):
        serializer = Product.objects.aggregate(total_price=Sum('price'))
        return Response(serializer)
