from rest_framework import serializers
from django.core.cache import cache
from .models import Ticket, Seat

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
        read_only_fields = ['user', 'created_at']

class SeatSerializer(serializers.ModelSerializer):
    current_status = serializers.SerializerMethodField()

    class Meta:
        model = Seat
        fields = ['id', 'seat_number', 'current_status']

    def get_current_status(self, obj):
        if hasattr(obj, 'ticket') or obj.status == 'BOUGHT':
            return 'BOUGHT'
        
        lock_key = f"seat_lock_{obj.id}"
        if cache.get(lock_key):
            return 'RESERVED'
            
        return 'AVAILABLE'