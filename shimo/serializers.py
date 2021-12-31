from rest_framework import serializers
from .models import Shimo

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shimo
        fields = ('id', 'on_air', 'segment', 'address',
                  'user', 'contents', 'answer', 'pt')
        fields = '__all__'