from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework import status


@api_view(['POST'])
def login(request: Request) -> Response:

    return Response(
        {'message': 'Login success'},
        status=status.HTTP_201_CREATED
    )
