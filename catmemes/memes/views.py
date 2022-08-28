from rest_framework.generics import ListCreateAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict

from .models import Meme
from .serializers import *


class MemeListAPIView(ListCreateAPIView):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer


class MemeUpdateAPIView(UpdateAPIView):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer
    lookup_field = "slug"


class MemeDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer
    lookup_field = "slug"

# class MemeAPIView(APIView):
#     def get(self, request):
#         memes = Meme.objects.all().values()
#         return Response({"memes": list(memes)})

#     def post(self, request):
#         serializer = MemeSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"new_meme": serializer.data})

#     def put(self, request, *args, **kwargs):
#         slug = kwargs.get('slug', None)
#         if not slug:
#             return Response({"error": "method PUT not allowed"})

#         try:
#             instance = Meme.objects.get(slug=slug)
#         except:
#             return Response({"error": "object not found"})
        
#         serializer = MemeSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"updated_post": serializer.data})