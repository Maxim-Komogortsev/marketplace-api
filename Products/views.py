from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer


class ProductViev(APIView):
    def get(self, request, prod_name=None):

        if not prod_name:
            all_products = Product.objects.all()
            return Response({'prods': ProductSerializer(all_products, many=True).data})

        products = Product.objects.filter(name=prod_name)
        return Response({'prods': ProductSerializer(products, many=True).data, 'query': prod_name})
    

    def post(self, request):
        
        new_prod = Product.objects.create(
            name = request.data['name'],
            desc = request.data['desc'],
            price = request.data['price']
        )

        return Response(model_to_dict(new_prod))