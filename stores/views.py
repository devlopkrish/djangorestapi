from django.shortcuts import render
from rest_framework import generics
from .serializers import PizzeriaListSerializer
from .models import Pizzeria
# Create your views here.

class PizzeriaListAPIView(generics.ListAPIView):
    queryset=Pizzeria.objects.all()
    serializer_class=PizzeriaListSerializer



class PizzaDetailViewById(generics.RetrieveAPIView):
    lookup_field='id'
    queryset=Pizzeria.objects.all()
    serializer_class=PizzeriaListSerializer


class CreatePizzaView(generics.CreateAPIView):
    queryset=Pizzeria.objects.all()
    serializer_class=PizzeriaListSerializer

class UpadatePizza(generics.RetrieveUpdateAPIView):
    lookup_field='id'
    queryset=Pizzeria.objects.all()
    serializer_class=PizzeriaListSerializer

class DeletePizza(generics.DestroyAPIView):
    lookup_field='id'
    queryset=Pizzeria.objects.all()