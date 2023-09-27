from rest_framework.serializers import ModelSerializer
from .models import Users, ProductCategory

class UsersSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'  #to specify which fields to serialize fields = ['lastname', 'fisrtname']


class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'  #to specify which fields to serialize fields = ['lastname', 'fisrtname']