from rest_framework import serializers
from . models import *

class untukApi(serializers.ModelSerializer):
    class Meta:
        model = Pelanggan
        fields = '__all__'
