from django.shortcuts import render

from .models import Reporting
from .serializers import ReportingSerializer

from rest_framework import generics, filters

class ReportingList(generics.ListCreateAPIView):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Reporting.objects.all()
    serializer_class = ReportingSerializer

class ReportingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reporting.objects.all()
    serializer_class = ReportingSerializer
