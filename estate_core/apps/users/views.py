from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    사용자 뷰셋
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        현재 로그인한 사용자만 자신의 정보를 볼 수 있도록 함
        """
        return User.objects.filter(id=self.request.user.id) 