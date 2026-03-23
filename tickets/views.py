from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.cache import cache
from .models import Ticket, Seat
from .serializers import TicketSerializer, SeatSerializer

class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SeatViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        session_id = self.request.query_params.get('session')
        if session_id:
            queryset = queryset.filter(session_id=session_id)
        return queryset

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def reserve(self, request, pk=None):
        seat = self.get_object()

        if hasattr(seat, 'ticket') or seat.status == 'BOUGHT':
            return Response(
                {'detail': 'Este assento já foi comprado e não pode ser reservado.'}, 
                status=status.HTTP_409_CONFLICT
            )

        lock_key = f"seat_lock_{seat.id}"
        timeout_seconds = 600 
        lock_acquired = cache.add(lock_key, request.user.id, timeout=timeout_seconds)
        
        if not lock_acquired:

            current_lock_owner = cache.get(lock_key)
            if current_lock_owner == request.user.id:
                return Response(
                    {'detail': 'Você já possui a reserva temporária deste assento.'},
                    status=status.HTTP_200_OK
                )
            
            return Response(
                {'detail': 'Assento temporariamente reservado por outro usuário.'}, 
                status=status.HTTP_409_CONFLICT
            )

        return Response(
            {'detail': f'Assento {seat.seat_number} reservado com sucesso por 10 minutos.'}, 
            status=status.HTTP_200_OK
        )