from rest_framework import serializers
from scripts.models import *


class CommandScriptSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=False)
    dependency = serializers.FileField(required=False)

    class Meta:
        model = BaseScript
        fields = ['script', 'requirements', 'scriptType']


class PatternsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patterns
        fields = ['syntax']


class ParametersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameters
        fields = ['name']


class BaseCommandSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    patterns = PatternsSerializer(many=True, required=False)
    parameters = ParametersSerializer(many=True, required=False)
    script_data = CommandScriptSerializer(many=False, required=False)

    class Meta:
        model = BaseCommand
        fields = (
            "id",
            "name",
            "description",
            "patterns",
            "parameters",
            "icon",
            "script_data",
        )


class BaseCommandCopySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    patterns = PatternsSerializer(many=True, required=False)
    parameters = ParametersSerializer(many=True, required=False)
    script_data = CommandScriptSerializer(many=False, required=False)

    class Meta:
        model = BaseCommand
        fields = (
            "id",
            "name",
            "description",
            "patterns",
            "parameters",
            "icon",
            "script_data",
        )
