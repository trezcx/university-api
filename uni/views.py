from rest_framework import viewsets
from .serializers import UniversitySerializer, UserSerializer
from .models import University, User

class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    pagination_by = 5

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_by = 5
