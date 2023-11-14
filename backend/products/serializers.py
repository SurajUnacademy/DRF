from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only = True) # to change the existing name of model in serializer
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]

    def get_my_discount(self,obj):
        try:
            return obj.get_discount()
        except:
            return None
