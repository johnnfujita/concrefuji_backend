from django.shortcuts import render
from rest_framework import generics, status, filters
from rest_framework.response import Response
from .models import Obra, Empresa, CPGroup, CP
from .serializers import CPSerializer, CPGroupSerializer, EmpresaSerializer, ObraSerializer, UserSerializer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

from django.contrib.auth.decorators import user_passes_test

class EmpresaList(generics.ListCreateAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    name = 'empresas-list'

class EmpresaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    name = 'empresas-detail'

class ObraList(generics.ListCreateAPIView):
    queryset = Obra.objects.all()
    serializer_class = ObraSerializer
    name = 'obras-list'

class ObraDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Obra.objects.all()
    serializer_class = ObraSerializer
    name = 'obras-detail'

class CPGroupList(generics.ListCreateAPIView):
    queryset = CPGroup.objects.all()
    serializer_class = CPGroupSerializer
    name = 'cpgroups-list'

class CPGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CPGroup.objects.all()
    serializer_class = CPGroupSerializer
    name = 'cpgroups-detail'


class CPList(generics.ListCreateAPIView):
    queryset = CP.objects.all()
    serializer_class = CPSerializer
    name = 'cps-list'

class CPDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CP.objects.all()
    serializer_class = CPSerializer
    name = 'cps-detail'



@api_view(["POST"])
@user_passes_test(lambda u: u.is_superuser)
def create_user(request):
    print('hleooso')
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {'data': serializer.data},
            status=status.HTTP_201_CREATED
        )
    return Response(
        {'data': serializer.errors},
        status=status.HTTP_400_BAD_REQUEST
    )