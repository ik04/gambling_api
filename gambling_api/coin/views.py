from rest_framework.views import APIView
from random import randrange
from rest_framework.response import Response
from rest_framework import status

# todo: learn actions for future
class CoinApi(APIView):
    def get(self,request):
        coin = randrange(2)
        result = "heads" if coin == 0 else "tails"
        return Response({"result":result},status=status.HTTP_200_OK)
