from django.shortcuts import render
from . models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from . serializer import untukApi

@api_view(['GET'])
def index(request):
    list_url = {
        'lihat-data': 'lihat-data',
        'buat-data':  'buat-data',
        'ubah-data':  'ubah-data',
        'hapus-data': 'hapus-data'
    }
    return Response(list_url)

@api_view(['GET'])
def lihatData(request):
    datanya = Pelanggan.objects.all()
    serialize = untukApi(datanya, many=True)
    return Response(serialize.data)

@api_view(['POST'])
def buatData(request):
    form = untukApi(data=request.data)
    if form.is_valid():
        form.save()
    return Response(form.data)

@api_view(['POST'])
def ubahData(request, pk):
    datanya = Pelanggan.objects.get(id=pk)
    serial = untukApi(instance=datanya, data=request.data)
    if serial.is_valid():
        serial.save()
    return Response(serial.data)

@api_view(['DELETE'])
def hapusData(request, pk):
    datanya = Pelanggan.objects.get(id=pk)
    datanya.delete()
    return Response("Data berhasil di hapus")
    
