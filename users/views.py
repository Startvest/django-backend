from rest_auth.registration.views import RegisterView
from .serializers import UserSerializer


class UserRegisterView(RegisterView):
    serializer_class = UserSerializer