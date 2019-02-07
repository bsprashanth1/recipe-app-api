from django.shortcuts import render
from requests import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from APIModel.models import UIModel
from APIModel.serializers import UISerializer


class UIList(generics.ListCreateAPIView):
    queryset = UIModel.objects.all()
    serializer_class = UISerializer

class UIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UIModel.objects.all()
    serializer_class = UISerializer

# class AIList(generics.ListCreateAPIView):
#     queryset = AIModel.objects.all()
#     serializer_class = AISerializer
#
# class AIDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = AIModel.objects.all()
#     serializer_class = AISerializer


