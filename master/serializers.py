from rest_framework import serializers
from .models import TaksModel

class TaksSerializers(serializers.ModelSerializer):
    class Meta:
        model = TaksModel
        # fields = ['title', 'content']
        fields = '__all__'
