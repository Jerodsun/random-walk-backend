from rest_framework import serializers

from .models import SampleData, BlackScholes

class SampleInputSerializer(serializers.ModelSerializer):
    """ The InputSerializer exposes which fields are required to be POSTed """
    class Meta:
        model = SampleData
        fields = ['id', 'created', 'direction']

class BlackScholesSerializer(serializers.ModelSerializer):
    """ Need a better description for what a serializer does """
    # https://www.django-rest-framework.org/tutorial/1-serialization/
    id = serializers.IntegerField(read_only=True)
    price = serializers.FloatField()
    strike = serializers.FloatField()
    interest_rate = serializers.FloatField()
    volatility = serializers.FloatField()
    time_to_exp = serializers.IntegerField()

    class Meta:
        model = BlackScholes
        fields = ['id', 'created', 'price', 'strike', 'interest_rate', 'volatility', 'time_to_exp']

    def create(self, validated_data):
        return BlackScholes.objects.create(**validated_data)