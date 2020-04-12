from rest_framework import serializers, fields
from . models import Project, Stage



class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = ('id', 'stage_name', 'stage_details', 'project' )

class ProjectSerializer(serializers.ModelSerializer):
    stage = StageSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = [
                'id',
                'project_name',
                'stage'
                ]

