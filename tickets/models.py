from django.db import models
from django.conf import settings
from movies.models import Session

class Seat(models.Model):
    # As 3 opções de estado que o desafio exige:
    STATUS_CHOICES = [
        ('AVAILABLE', 'Disponível'),
        ('RESERVED', 'Reservado'),
        ('BOUGHT', 'Comprado'),
    ]

    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='seats')
    seat_number = models.CharField(max_length=10, verbose_name="Número do Assento (Ex: A1)")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='AVAILABLE')
    
    # Quem reservou/comprou e quando? (Nulo inicialmente porque a cadeira começa vazia)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    reserved_at = models.DateTimeField(null=True, blank=True, verbose_name="Horário da Reserva")

    class Meta:
        # Garante que não existem duas cadeiras "A1" na mesma sessão
        unique_together = ('session', 'seat_number')

    def __str__(self):
        return f"{self.seat_number} - {self.get_status_display()}"


class Ticket(models.Model):
    # O Bilhete (Ticket) agora exige sempre um utilizador e um assento (seat)!
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tickets')
    seat = models.OneToOneField(Seat, on_delete=models.CASCADE, related_name='ticket')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bilhete: {self.seat.seat_number} ({self.user.username})"