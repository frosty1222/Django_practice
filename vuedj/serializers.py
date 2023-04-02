from rest_framework import routers,serializers,viewsets
from .models import Product
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    product_image = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Product
        fields = ['id','name','description','price','product_image']
        
    def create(self, validated_data):
        product_image = validated_data.pop('product_image')
        instance = self.Meta.model(**validated_data)
        if product_image:
            instance.product_image.save(product_image.name, product_image)
        instance.save()
        return instance