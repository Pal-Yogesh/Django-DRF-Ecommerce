from rest_framework import serializers

from .models import Brand, Category, Nproduct


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class NproductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nproduct
        fields = "__all__"
