from rest_framework import serializers
from rest_framework import generics
from .models import Women

class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = "__all__"

