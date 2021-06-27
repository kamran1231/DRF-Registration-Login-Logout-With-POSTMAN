from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import RegistrationSerializer
from rest_framework.response import Response

# Create your views here.


@api_view(['GET','POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)




