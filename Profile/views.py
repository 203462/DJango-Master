# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
import os
import json 

#Importaciones de modelos
from Profile.models import Profile


#Importacion de serializers
from Profile.serializers import ProfileSerializer

class ProfileTable(APIView):

    def get_objectUser(self, idUser):
        try:
            return User.objects.get(pk = idUser)
        except User.DoesNotExist:
            return "No encontrado"

    def post(self, request):
        idUser = request.data['id_user']
        userUpdate = request.data
        user = self.get_objectUser(idUser)
        if(user != "No encontrado"):
            serializer = ProfileSerializer(data=userUpdate)
            if serializer.is_valid():
                validated_data = serializer.validated_data
                profile = Profile(**validated_data)
                profile.save()
                user = User.objects.filter(id=idUser)
                user.update(username=userUpdate.get('username'))
                user.update(first_name=userUpdate.get('first_name'))
                user.update(last_name=userUpdate.get('last_name'))
                user.update(email=userUpdate.get('email'))
                serializer_response = ProfileSerializer(profile)
                return Response(serializer_response.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Usuario no encontrado")
    
class ProfileTableDetail(APIView):
    def get_object(self, pk):
        try:
            return Profile.objects.get(id_user = pk)
        except Profile.DoesNotExist:
            return "No encontrado"

    def responseCus(self,user,data, status):
        responseJson = {
            "first_name":user[0]['first_name'],
            "last_name":user[0]['last_name'],
            "username":user[0]['username'],
            "email":user[0]['email'],
            "id_user":data.get('id_user'),
            "url_img":data.get('url_img'),
            "status":status
        }
        response = json.dumps(responseJson)
        responseCustom = json.loads(response)
        return responseCustom

    def get(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        user = User.objects.filter(id=pk).values()
        if idResponse != "No encontrado":
            idResponse = ProfileSerializer(idResponse)
            responseCustom = self.responseCus(user,idResponse.data,status.HTTP_200_OK)
            return Response(responseCustom)
        else:
            errorData = {
                "url_img" : "/assets/img-profile/default.jpg",
                "id_user" : pk
            }
        responseCustom = self.responseCus(user,errorData,status.HTTP_400_BAD_REQUEST)
        return Response(responseCustom)
    
    def put(self, request, pk, format=None):
        archivos = request.data['url_img']
        userUpdate = request.data
        idResponse = self.get_object(pk)
        if(idResponse != "No encontrado"):
            user = User.objects.filter(id=pk)
            user.update(username=userUpdate.get('username'))
            user.update(first_name=userUpdate.get('first_name'))
            user.update(last_name=userUpdate.get('last_name'))
            user.update(email=userUpdate.get('email'))
            serializer = ProfileSerializer(idResponse)
            try:
                if(archivos == ""):
                    archivos = idResponse.url_img
                else:
                    os.remove('assets/'+str(idResponse.url_img))
            except os.error:
                print("Archivo no encontrado")
            idResponse.url_img = archivos
            idResponse.save()
            responseCustom = self.responseCus(user.values(),serializer.data,status.HTTP_201_CREATED)
            return Response(responseCustom)
        else:
            return Response("No hay registros")