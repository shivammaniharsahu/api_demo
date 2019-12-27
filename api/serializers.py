from rest_framework import serializers
from .models import Basicinfo


class apiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basicinfo
        fields = ('id','name', 'email', 'phoneno')
