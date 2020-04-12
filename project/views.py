from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from . models import Project, Stage
from . serializers import ProjectSerializer, StageSerializer


class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve, update or delete a code snippet.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
