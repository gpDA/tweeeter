from main.models import Main
from main.serializers import MainSerializer
from rest_framework import generics

class MainListCreate(generics.ListCreateAPIView):
    queryset = Main.objects.all()
    serializer_class = MainSerializer