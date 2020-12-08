from django.contrib.auth.models import User
from rest_framework import serializers
from amazonprices.models import Items

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'profile')

class ItemsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Items
        fields = ('url', 'date', 'user')
