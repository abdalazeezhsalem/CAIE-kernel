from rest_framework import serializers
from ..models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title','author','content','categories')
        # fields = ('__all__')

