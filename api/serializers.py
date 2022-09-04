from rest_framework import serializers

from backend.models import *

class NewsBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsBlog
        fields = [
            'id',
            'title',
            'content',
            'news_image',
            'allow_public_comments',
            'date_created',
            'user_comment',
            'slug',
            'absolute_url',
        ]