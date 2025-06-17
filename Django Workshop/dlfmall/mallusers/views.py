from rest_framework.views import APIView
from django.http import JsonResponse
from .serializers import*
from.models import*

class userSignup(APIView):
    def post(self,request):
        serializers = userDetailsSerializer(data=request.data)
        if serializers.is_valid():
            userDetails.objects.create(**serializerData.data)
            message ={"message":"User Signup successfully"}
            return JsonResponse(message)
        return JsonResponse(serializerData.errors)

