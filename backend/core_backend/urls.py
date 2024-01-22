from django.urls import path
from .views import functions_room, functions_users, functions_reservations

users_url = [
    path('create_user', functions_users.create_user, name='create_user'),
    path('get_users', functions_users.get_users, name='get_users'),
    path('get_user', functions_users.get_user, name='get_user'),
    path('update_user', functions_users.update_user, name='update_user'),
    path('delete_user', functions_users.delete_user, name='delete_user'),
]

rooms_url = [
    path('create_room', functions_room.create_room, name='create_room'),
    path('get_rooms', functions_room.get_rooms, name='get_rooms'),
    path('update_room', functions_room.update_room, name='update_room'),
    path('delete_room', functions_room.delete_room, name='delete_room'),
]

reservations_url = [
    path('create_reservation', functions_reservations.create_reservation, name='create_reservation'),
    path('get_reservations', functions_reservations.get_reservations, name='get_reservations'),
]

urlpatterns = users_url + rooms_url + reservations_url