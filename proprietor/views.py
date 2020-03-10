from django.shortcuts import render
from .serializer import PersonSerializer
from rest_framework import generics
from .models import Person
from rest_framework import viewsets


# class PersonView(generics.ListAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer

class PersonApiView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
