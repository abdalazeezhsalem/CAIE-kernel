from rest_framework import viewsets, status, settings
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..serializers import UserSerializer
from ..models import User

#| Successfully created             |               `201 Created` |

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['POST'])
def create_new_user(request):
    serializer = UserSerializer(data=request.data)

    try:
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    except :
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






