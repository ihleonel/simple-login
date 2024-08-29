from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework import status


class Login(APIView):
    def post(request: Request) -> Response:
        return Response({'message': 'success'}, status=status.HTTP_200_OK)
