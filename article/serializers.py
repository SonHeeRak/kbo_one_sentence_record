from rest_framework import serializers
from . import baseball_models as b_models
from . import daily_news_models as d_models


class HitterRecordSerializer(serializers.ModelSerializer):
    # Serializers define the API representation.
    class Meta:
        model = b_models.Hitter
        fields = '__all__'


class PitcherRecordSerializer(serializers.ModelSerializer):
    # Serializers define the API representation.
    class Meta:
        model = b_models.Pitcher
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    # Serializers define the API representation.
    class Meta:
        model = b_models.Person
        fields = '__all__'


class GamecontappSerializer(serializers.ModelSerializer):
    # Serializers define the API representation.
    class Meta:
        model = b_models.Gamecontapp
        fields = '__all__'


class CommonDynamicVariableSerializer(serializers.ModelSerializer):
    class Meta:
        model = d_models.CommonDynamicVariable
        fields = '__all__'
