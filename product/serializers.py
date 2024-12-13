from rest_framework import serializers

from .models import Product,ProductImages,Review



class BaseSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('id', 'created_at', 'updated_at', 'is_active')
        fields_read_only = ('id', 'created_at', 'updated_at')





class ProductImagesSerializer(BaseSerializer):

    class Meta:
        model = ProductImages
        fields = '__all__'


class ProductSerializer(BaseSerializer):

    images = ProductImagesSerializer(many = True, read_only = True)
    reviews = serializers.SerializerMethodField(method_name = 'get_reviews', read_only = True)
# A read-only field that get its representation from calling a method on the parent serializer class.
#  The method called will be of the form "get_{field_name}", and should take a single argument,
#  which is the object being serialized.

    class Meta:
        model = Product
        fields = ('id', 'created_at', 'updated_at', 'name', 'description', 'price', 'brand', 'category',
                  'ratings', 'stock', 'user','reviews', 'images')

        extra_kwargs = {
            "name": {"required": True, "allow_blank": False},
            "description":{"required": True, "allow_blank": True}
        }

    def get_reviews(self, obj):
            
        reviews = obj.reviews.all()
        serializer = ReviewSerializer(reviews, many = True)
        return serializer.data

    



class ReviewSerializer(BaseSerializer):

    class Meta:
        model = Review
        fields = '__all__'