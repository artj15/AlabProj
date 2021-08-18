from django.shortcuts import render
from django.db.models import Sum
from rest_framework import generics, viewsets
from rest_framework.response import Response
from .serializer import ProductSerializer, ProductCount
from .models import Product


# Create your views here.


class ProductApi(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, format=None):
        serializer = ProductSerializer(Product.objects.all(), many=True)
        return Response(serializer.data)



    # def delete(self, request, pk):
    #     pos = get_object_or_404(Product.objects.all(), pk=pk)
    #     pos.delete()
    #     return Response({
    #         "message": "Позиция`{}` has been deleted.".format(pk)
    #     }, status=204)


class ProductCount(generics.GenericAPIView):
    queryset = Product.objects.aggregate(total_price=Sum('price'))
    serializer_class = ProductCount

    def get(self, request, format=None):
        serializer = Product.objects.aggregate(total_price=Sum('price'))
        return Response(serializer)
