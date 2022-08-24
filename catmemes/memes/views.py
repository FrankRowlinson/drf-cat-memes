from django.shortcuts import render
from rest_framework import generics
from .models import Meme
from .serializers import *


class MemeAPIView(generics.ListAPIView):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer
