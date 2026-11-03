from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..serializers import CommentSerializer
from ..models import Comment


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

@api_view(['POST'])
def create_comment(request):
    serializer = CommentSerializer(data=request.data)
    try:
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    except :
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
