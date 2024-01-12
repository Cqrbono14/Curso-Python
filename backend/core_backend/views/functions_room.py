from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from core_backend.models import Sala
from voluptuous.schema_builder import Required
from backend.utils import validate_data

@api_view(['GET'])
@permission_classes([AllowAny])
def get_rooms(request):
    rooms = Sala.objects.all()
    response = []
    for room in rooms:
        response.append({
            'id': room.id,
            'nombre': room.nombre,
            'tamanio': room.tamanio,
            'ubicacion': room.ubicacion,
            'aforo': room.aforo
        })
    return Response(response, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([AllowAny])
def create_room(request):
    data = validate_data({
        Required('nombre'):str,
        ('tamanio'):int,
        ('ubicacion'):str,
        ('aforo'):int
    }, request.data)

    if 'tamanio' not in data:
        data['tamanio'] = None
    if 'ubicacion' not in data:
        data['ubicacion'] = None
    if 'aforo' not in data:
        data['aforo'] = None

    room = Sala.objects.create(nombre = data['nombre'], tamanio = data['tamanio'], ubicacion = data['ubicacion'], aforo = data['aforo'])
    room.save()
    return Response("Sala creada correctamente", status=status.HTTP_201_CREATED)

@api_view(['PUT'])
@permission_classes([AllowAny])
def update_room(request):
    data = validate_data({
        Required('id'):int,
        ('nombre'):str,
        ('tamanio'):int,
        ('ubicacion'):str,
        ('aforo'):int
    }, request.data)

    try:
        room = Sala.objects.get(id = data['id'])
        if 'nombre' in data:
            room.nombre = data['nombre']
        if 'tamanio' in data:
            room.tamanio = data['tamanio']
        if 'ubicacion' in data:
            room.ubicacion = data['ubicacion']
        if 'aforo' in data:
            room.aforo = data['aforo']
        room.save()
        return Response("Sala modificada correctamente", status=status.HTTP_200_OK)
    except:    
        return Response("La sala que deseas modificar no existe", status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_room(request):
    data = validate_data({
        Required('id'):int
    }, request.data)

    try:
        room = Sala.objects.get(id = data['id'])
        room.delete()
        return Response("Sala eliminada correctamente", status=status.HTTP_200_OK)
    except:
        return Response("La sala que deseas eliminar no existe", status=status.HTTP_404_NOT_FOUND)