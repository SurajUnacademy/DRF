import json
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from products.models import Product
from products.serializers import ProductSerializer

# Create your views here. 
# we can have multiple serializer for a single model

@api_view(["GET","POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API VIEW
    """
    serializer = ProductSerializer(data = request.data)   # using serializer we can check that the data sent over post request is valid or not
    if serializer.is_valid(): 
        instance = serializer.save()
        print("instance = ", instance)
        return Response(data = serializer.data)



    # instance = Product.objects.all().order_by("?").first()
    # data = {}
    # if instance:
    #     data = ProductSerializer(instance).data # so this makes it a class of instance and data is fetched as its property.
    # return Response(data) #using serializer this data is sended as json



    # # request -> http request -> from Django ( no relation with python reuests) = instance of HttpRequest
    # print(request.GET) # url query params
    # print(request.POST)
    # body = request.body # byte string of json data
    # data = {}
    # try:
    #     data = json.loads(body) # string of json data -> python dictionary
    # except:
    #     pass
    # print(data)
    # data['params'] = dict(request.GET)
    # data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type
    # return JsonResponse(data)