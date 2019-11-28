from rest_framework import serializers
from .models import Form


class Formserializer(serializers.ModelSerializer):
    class Meta:
        model=Form
        fields='__all__'
