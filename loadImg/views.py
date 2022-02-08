# Create your views here.
from distutils.log import info
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions
import os.path

#Importaciones de modelos
from loadImg.models import LoadImage

#IMportacion de serializers
from loadImg.serializers import LoadImageSerializers

class LoadImageTable(APIView):
    def get(self, request, format=None):
        queryset = LoadImage.objects.all()
        serializer = LoadImageSerializers(queryset, many = True, context = {'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        
        if 'url_img' not in request.data:
            raise exceptions.ParseError(
                "No has seleccionado el archivo a subir")
        info = request.data['url_img']
        name, formato = os.path.splitext(info.name)
        request.data['name_img'] = name
        request.data['format_img'] = formato
        serializer = LoadImageSerializers(data=request.data)    
        
        
        if serializer.is_valid():
            validated_data = serializer.validated_data
            img = LoadImage(**validated_data)
            img.save()
            serializer_response = LoadImageSerializers(img)
            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoadImageTableDetail(APIView):
    
    
    def get_object(self, pk):
        try:
            return LoadImage.objects.get(pk = pk)
        except LoadImage.DoesNotExist:
            return 0

    def get(self,request ,pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 0:
            idResponse = LoadImageSerializers(idResponse)
            return Response(idResponse.data, status = status.HTTP_200_OK)
        return Response("No datos", status = status.HTTP_400_BAD_REQUEST)


    def put(self, request,pk, format=None):
        
        idResponse = self.get_object(pk)
        info = request.data['url_img']
        name, formato = os.path.splitext(info.name)
        request.data['name_img'] = name
        request.data['format_img'] = formato
        serializer = LoadImageSerializers(idResponse, data = request.data)
        
        
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas, status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        aBorrar = self.get_object(pk)
        if aBorrar != 0:
            aBorrar.url_img.delete(save=True)
            aBorrar.delete()
            return Response("Dato eliminado",status=status.HTTP_204_NO_CONTENT)
        return Response("Dato no encontrado",status = status.HTTP_400_BAD_REQUEST)
