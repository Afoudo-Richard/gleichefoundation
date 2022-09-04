from django.shortcuts import render
from .serializers import *
from backend.models import *


from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class NewsBlogList(APIView):

    def get(self, request, format=None):
        news_blogs = NewsBlog.objects.all()
        serializer = NewsBlogSerializer(news_blogs, many=True)
        return Response(serializer.data)
