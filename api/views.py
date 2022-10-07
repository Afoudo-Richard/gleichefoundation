from django.shortcuts import render
from .serializers import *
from backend.models import *
from .pagination import *


from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class NewsBlogList(APIView):
    pagination_class = CustomPagination

    def get(self, request, format=None):
        news_blogs = NewsBlog.objects.filter(publish=1).order_by('-date_created')
        paginator = CustomPagination()
        paginator.default_limit = 1
        result_page = paginator.paginate_queryset(news_blogs, request)
        serializer = NewsBlogSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
