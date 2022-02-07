from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import json

# Importaciones de modelos 
from primerComponente.models import PrimerTabla

# Importaciones de serializadores
from primerComponente.serializers import PrimerTablaSerializer
# Create your views here.


class PrimerTablaList(APIView):
    
    def aJson(self,datos,mensaje ,status):
        json0={"messages":mensaje, "pay_load":datos, "status": status }
        json1=json.dumps(json0)
        json2 = json.loads(json1)
        return json2
    
    
    def get(self, request, format=None):
        queryset = PrimerTabla.objects.all()
        serializer = PrimerTablaSerializer(queryset,many=True,context={'request':request})
        response=self.aJson(serializer.data,"succes" , "200-ok")
        return Response(response)

    def post(self, request, format=None):
        serializer = PrimerTablaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas,status =status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    

class PrimerTablaDetail(APIView):
    def get_object(self, pk):
        try:
            return PrimerTabla.objects.get(pk = pk)
        except PrimerTabla.DoesNotExist:
            return 0
    
    def get(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 0:
            idResponse = PrimerTablaSerializer(idResponse)
            return Response(idResponse.data, status = status.HTTP_200_OK)
        return Response("No hay datos en la base de datos bro, lo siento",status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        serializer = PrimerTablaSerializer(idResponse, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas,status =status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
    
        aBorrar = self.get_object(pk)
        if aBorrar!="Dato a borar no encontrado":
            aBorrar.delete()
            return Response("ok" ,status=status.HTTP_200_OK)
        else:
            return Response("dato no encontrado",status=status.HTTP_400_BAD_REQUEST)
        
        
