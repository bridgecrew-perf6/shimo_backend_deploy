from django.shortcuts import render

# Create your views here.
from rest_framework import status, viewsets, serializers, generics
from django_filters import rest_framework as filters

from .models import Shimo
from .serializers import PostSerializer




class ListYato(generics.ListCreateAPIView):
    queryset = Shimo.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Shimo.objects.all()
        user = self.request.query_params.get('user', None)
        address = self.request.query_params.get('address', None)
        segment = self.request.query_params.get('segment', None)
        contents = self.request.query_params.get('contents', None)
        answer = self.request.query_params.get('answer', None)
        on_air = self.request.query_params.get('on_air', None)
        pt = self.request.query_params.get('pt', None)
        page = self.request.query_params.get('page', None)

        if user is not None:
            queryset = queryset.filter(user__icontains=user)
        if address is not None:
            queryset = queryset.filter(address__icontains=address)
        if segment is not None:
            queryset = queryset.filter(segment=segment)
        if contents is not None:
            queryset = queryset.filter(contents__icontains=contents)
        if answer is not None:
            queryset = queryset.filter(answer__icontains=answer)
        if on_air is not None:
            queryset = queryset.filter(on_air=on_air)
        if pt is not None:
            queryset = queryset.filter(pt=pt)
        if page is not None:
            queryset = queryset.filter(page=page)
        return queryset