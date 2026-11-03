from pickle import TRUE

from django.db import IntegrityError
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..serializers import CategorySerializer
from ..models import Category


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

@api_view(['POST'])
def create_new_category(request):
    serializer = CategorySerializer(data=request.data)
    try:
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    except IntegrityError:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


