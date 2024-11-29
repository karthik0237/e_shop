from rest_framework.serializers import ModelSerializer

from .models import Product,ProductImages



class BaseSerializer(ModelSerializer):
    
    class Meta:
        fields = ['id', 'created_at', 'updated_at', 'is_active']
        fields_read_only = ['id', 'created_at', 'updated_at']





class ProductImagesSerializer(BaseSerializer):

    class Meta:
        model = ProductImages
        fields = '__all__'


class ProductSerializer(BaseSerializer):

    images = ProductImagesSerializer(many = True, read_only = True)

    class Meta:
        model = Product
        fields = ('id', 'created_at', 'updated_at', 'name', 'description', 'price', 'brand', 'category',
                  'ratings', 'stock', 'user', 'images')

        extra_kwargs = {
            "name": {"required": True, "allow_blank": False},
            "description":{"required": True, "allow_blank": True}

        }