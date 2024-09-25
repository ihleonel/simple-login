from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from auth.domain.user import User


class Login(APIView):
    def post(self, request: Request) -> Response:
        username = request.data.get('username')
        password = request.data.get('password')

        user = User(username, password)
        if not user.is_valid():
            return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)

        user_auth = authenticate(
            username=user.username, password=user.password
        )
        if user_auth is None:
            return Response(
                data={'non_field': 'Invalid Username or Password'},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            refresh = RefreshToken.for_user(user_auth)
            return Response(
                data={
                    'access': str(refresh.access_token),
                    'refresh': str(refresh)
                },
                status=status.HTTP_200_OK
            )
        except Exception:
            return Response(
                data={'non_field': 'Invalid Username or Password'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
