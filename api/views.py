from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Basicinfo
from .serializers import apiSerializer
from  rest_framework import status
# Create your views here.


@api_view(['GET','POST'])
def api_list(request):
    if request.method == 'GET':
        obj = Basicinfo.objects.all()
        serializer = apiSerializer(obj, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = apiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def api_detail(request,pk):
    try:
        obj = Basicinfo.objects.get(id=pk)
    except Basicinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = apiSerializer(obj)
    return Response(serializer.data)
