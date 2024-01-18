from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from core_backend.models import Usuario
from voluptuous.schema_builder import Required
from backend.utils import validate_data
from django.db import IntegrityError
import random

@api_view(['GET'])
@permission_classes([AllowAny])
def get_users(request):
    users = Usuario.objects.all()
    response = []
    for user in users:
        response.append({
            'id': user.id,
            'nombre': user.nombre,
            'apellido': user.apellido,
            'identificador': user.identificador
        })
    return Response(response, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_user(request):
    data = validate_data({
        Required('identificador'):int
    }, request.data)

    try:
        user = Usuario.objects.get(identificador = data['identificador'])
        response = {
            'id': user.id,
            'nombre': user.nombre,
            'apellido': user.apellido,
            'identificador': user.identificador
        }
        return Response(response, status=status.HTTP_200_OK)
    except:
        return Response("Usuario no encontrado", status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):
    data = validate_data({
        Required('nombre'): str,
        ('apellido'): str,
    }, request.data)

    if 'apellido' not in data:
        data['apellido'] = None

    try:
        identificador = generar_id()
        user = Usuario.objects.create(nombre=data['nombre'], apellido=data['apellido'], identificador=identificador)
        user.save()
        return Response("Usuario creado correctamente", status=status.HTTP_201_CREATED)
    except IntegrityError:
        return create_user(request)

def generar_id():
    while True:
        nuevo_id = random.randint(1000, 9999)
        if not Usuario.objects.filter(identificador=nuevo_id).exists():
            return nuevo_id

@api_view(['PUT'])
@permission_classes([AllowAny])
def update_user(request):
    data = validate_data({
        Required('identificador'):int,
        ('nombre'):str,
        ('apellido'):str,
    }, request.data)

    try:
        user = Usuario.objects.get(identificador = data['identificador'])
        if 'nombre' in data:
            user.nombre = data['nombre']
        if 'apellido' in data:
            user.apellido = data['apellido']
        user.save()
        return Response("Usuario actualizado correctamente", status=status.HTTP_200_OK)
    except:
        return Response("Usuario no encontrado", status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_user(request):
    data = validate_data({
        Required('identificador'):int
    }, request.data)

    try:
        user = Usuario.objects.get(identificador = data['identificador'])
        user.delete()
        return Response("Usuario eliminado correctamente", status=status.HTTP_200_OK)
    except:
        return Response("Usuario no encontrado", status=status.HTTP_404_NOT_FOUND)