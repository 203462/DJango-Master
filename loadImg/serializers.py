from rest_framework import serializers

#Modelo
from loadImg.models import LoadImage

class LoadImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = LoadImage
        fields = ('pk','name_img','format_img', 'url_img')