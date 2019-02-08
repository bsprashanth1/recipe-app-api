from django.contrib.auth.models import User
from rest_framework import serializers

from APIModel.models import UIModel


class UISerializer(serializers.HyperlinkedModelSerializer):
    request_id = serializers.ReadOnlyField(source='UIModel.request_id')
    class Meta:
        model = UIModel
        fields = ['request_id','inputText', 'inputType', 'keywords', 'totalScenarios']

# class AISerializer(serializers.HyperlinkedModelSerializer):
#     UserInput = UISerializer(read_only=True)
#
#     class Meta:
#         model = AIModel
#         fields = ['UserInput','keywords']

class JiraSerializer(serializers.ALL_FIELDS):
    pass