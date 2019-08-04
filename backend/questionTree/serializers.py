from rest_framework import serializers

from .models import WebApp, Requirement, Industry

class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = ['id','requirement', 'obligatory', 'answer',]

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ('id','industry',)

class WebAppSerializer(serializers.ModelSerializer):
    industries = IndustrySerializer(many=True)
    requirements = RequirementSerializer(many=True)
    class Meta:
        model = WebApp
        fields = ('id','title', 'requirements', 'industries',)
