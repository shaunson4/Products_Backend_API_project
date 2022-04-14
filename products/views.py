from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Products

@api_view(['GET', 'POST'])
def products_list(request):    
    if request.method == 'GET':
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def products_detail(request, pk):
    try:
        products = Products.objects.get(pk=pk)
        serializer = ProductSerializer(products)
        return Response(serializer.data)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

   
          

