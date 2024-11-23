from rest_framework.serializers import ModelSerializer

from .models import Product



class BaseSerializer(ModelSerializer):
    
    class Meta:
        fields = ['id', 'created_at', 'updated_at', 'is_active']
        fields_read_only = ['id', 'created_at', 'updated_at']



class ProductSerializer(BaseSerializer):

    class Meta:
        model = Product
        fields = '__all__'
