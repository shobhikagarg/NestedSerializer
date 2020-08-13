#noinspection PyUnresolvedReferences
from django.shortcuts import render
#noinspection PyUnresolvedReferences
from django.utils import six
#noinspection PyUnresolvedReferences
from django.http import Http404
#noinspection PyUnresolvedReferences
from rest_framework import status, generics
#noinspection PyUnresolvedReferences
from rest_framework.response import Response
#noinspection PyUnresolvedReferences
from rest_framework.views import APIView
#noinspection PyUnresolvedReferences
from .models import *
#noinspection PyUnresolvedReferences
from .serializers import PersonSerializer,CountrySerializer,CitySerializer,StateReadSerializer,TownSerializer
#noinspection PyUnresolvedReferences
from rest_framework import viewsets
#noinspection PyUnresolvedReferences
from django.shortcuts import get_object_or_404
#noinspection PyUnresolvedReferences
from rest_framework.pagination import PageNumberPagination
#noinspection PyUnresolvedReferences
from django_filters.rest_framework import DjangoFilterBackend

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'

class PersonList(APIView):
    def get(self,request):
        queryset=Person.objects.all()
        serializer=PersonSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonList(generics.ListAPIView):
    queryset=Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields=('city',)
    pagination_class = LargeResultsSetPagination

class CountryViewset(viewsets.ViewSet):
    def list(self,request):
        queryset=Country.objects.all()
        serializer=CountrySerializer(queryset,many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,id=None):
        queryset = Country.objects.all()
        article=get_object_or_404(queryset,id=id)
        serializer = CountrySerializer(article)
        return Response(serializer.data)

class StateViewset(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateReadSerializer

class StateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StateReadSerializer
    queryset = State.objects.all()
