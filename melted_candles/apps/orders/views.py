
from rest_framework.views import APIView
from rest_framework.response import Response

class CreateOrder(APIView):

    
    def post(self, request):
        print("post")