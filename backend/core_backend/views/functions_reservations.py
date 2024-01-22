from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from core_backend.models import Reservacion
from voluptuous.schema_builder import Required
from backend.utils import validate_data
from datetime import datetime, date , time
from core_backend.models import Sala, Usuario

@api_view(['GET'])
@permission_classes([AllowAny])
def get_reservations(request):
    reservations = Reservacion.objects.all()
    response = []
    for reservation in reservations:
        response.append({
            'id': reservation.id,
            'usuario': reservation.usuario.id,
            'sala': reservation.sala.id,
            'fecha': reservation.fecha,
            'hora_inicio': reservation.hora_inicio,
            'hora_fin': reservation.hora_fin,
            'personas': reservation.personas
        })
    return Response(response, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([AllowAny])
def create_reservation(request):
    data = validate_data({
        Required('usuario'): int,
        Required('sala'): str,
        Required('fecha'): str,
        Required('hora_inicio'): str,
        Required('hora_fin'): str,
        Required('personas'): int
    }, request.data)

    data['fecha'] = datetime.strptime(data['fecha'], '%Y-%m-%d').date()
    data['hora_inicio'] = datetime.strptime(data['hora_inicio'], '%H:%M:%S').time()
    data['hora_fin'] = datetime.strptime(data['hora_fin'], '%H:%M:%S').time()

    try:
        usuario = Usuario.objects.get(identificador=data['usuario'])

        sala = Sala.objects.get(nombre=data['sala'])

        duration = datetime.combine(date.today(), data['hora_fin']) - datetime.combine(date.today(), data['hora_inicio'])
        if duration.total_seconds() > 7200: 
            return Response("La duración de la reservación debe ser de máximo 2 horas", status=status.HTTP_400_BAD_REQUEST)
        elif duration.total_seconds() <= 0:
            return Response("La hora de inicio no puede ser mayor o igual a la hora de fin", status=status.HTTP_400_BAD_REQUEST)

        existing_reservations = Reservacion.objects.filter(
            sala_id=sala.id,
            fecha=data['fecha'],
            hora_fin__gt=data['hora_inicio'],
            hora_inicio__lt=data['hora_fin']
        )

        if existing_reservations.exists():
            return Response("Conflicto de horario con otra reservación en la misma sala y fecha", status=status.HTTP_400_BAD_REQUEST)

        if (data['fecha'] > date.today()):
            if (data['personas'] <= sala.aforo):
                reservation = Reservacion.objects.create(
                    usuario_id=usuario.id,
                    sala_id=sala.id,
                    fecha=data['fecha'],
                    hora_inicio=data['hora_inicio'],
                    hora_fin=data['hora_fin'],
                    personas=data['personas']
                )
                reservation.save()
                return Response("Reservacion creada correctamente", status=status.HTTP_201_CREATED)
            else:
                return Response("La cantidad de personas excede el aforo de la sala", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("La fecha de la reservacion no puede ser anterior o igual a la fecha actual", status=status.HTTP_400_BAD_REQUEST)

    except Usuario.DoesNotExist:
        return Response("Usuario no encontrado", status=status.HTTP_404_NOT_FOUND)
    except Sala.DoesNotExist:
        return Response("Sala no encontrada", status=status.HTTP_404_NOT_FOUND)