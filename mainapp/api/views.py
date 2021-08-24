from rest_framework.views import APIView
from rest_framework.response import Response


class TestApiView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {'id': 1, 'name': 'John'},
            {'id': 2, 'name': 'Jack'},
        ]
        return Response(data)
