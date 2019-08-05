from rest_framework import serializers

from .models import SampleData

class InputSerializer(serializers.ModelSerializer):
    """ The InputSerializer exposes which fields are required to be POSTed """
    class Meta:
        model = SampleData
        fields = ['id', 'created', 'direction']
