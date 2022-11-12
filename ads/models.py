from django.db import models
from rest_framework import serializers


class Ads(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    author = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    description = models.TextField(max_length=500, null=True, blank=True)
    address = models.CharField(max_length=60)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class AdsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    author = serializers.CharField(max_length=20)
    price = serializers.DecimalField(max_digits=10, decimal_places=0)
    description = serializers.CharField(max_length=500, allow_null=True)
    address = serializers.CharField(max_length=60)
    is_published = serializers.BooleanField(default=False)

    class Meta:
        model = Ads
        fields = '__all__'
