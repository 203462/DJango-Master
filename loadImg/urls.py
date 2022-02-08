from django.urls import re_path
from django.conf.urls import include

#Views
from loadImg.views import LoadImageTable,LoadImageTableDetail

urlpatterns = [
    re_path(r'^form/$', LoadImageTable.as_view()),
    re_path(r'^form/(?P<pk>\d+)$', LoadImageTableDetail.as_view()),    
]