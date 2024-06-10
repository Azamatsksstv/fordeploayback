from rest_framework_simplejwt.views import TokenObtainPairView

from accounts.serializers.user import CustomTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
