from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from rest_framework import viewsets
from .models import CustomUser
from .serializers import UsuarioSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from users.permissions import AdminPermission, CanAccessGhibliEndpoint
from rest_framework.permissions import IsAuthenticated
import requests

# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, AdminPermission]
    queryset = CustomUser.objects.all()
    serializer_class = UsuarioSerializer

    def perform_create(self, serializer):
        # Antes de guardar el usuario, encriptamos su contraseña
        password = self.request.data.get('password')
        encrypted_password = make_password(password)
        serializer.save(password=encrypted_password)
    
class GhibliEndpointView(APIView):
    permission_classes = [IsAuthenticated, CanAccessGhibliEndpoint]
    endpoint = None

    def get(self, request):
        if not self.endpoint:
            return Response({"error": "El endpoint no está configurado correctamente"}, status=500)

        # Realizar una solicitud GET al endpoint de Studio Ghibli
        response = requests.get(f"https://ghibliapi.vercel.app/{self.endpoint}")

        # Verificar el estado de la respuesta
        if response.status_code == 200:
            # Si la respuesta es exitosa, devolver los datos de la API de Studio Ghibli
            return Response(response.json())
        else:
            # Si la solicitud falla, devolver un mensaje de error
            return Response({"error": "No se pudo obtener la información de Studio Ghibli"}, status=response.status_code)