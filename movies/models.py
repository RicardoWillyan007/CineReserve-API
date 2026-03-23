from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name="Título")
    description = models.TextField(verbose_name="Descrição")
    duration = models.IntegerField(help_text="Duração em minutos", verbose_name="Duração")
    release_date = models.DateField(verbose_name="Data de Lançamento")

    def __str__(self):
        return self.title

class Session(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='sessions')
    room = models.CharField(max_length=50, verbose_name="Sala")
    start_time = models.DateTimeField(verbose_name="Horário de Início")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Preço do Ingresso")

    def __str__(self):
        return f"{self.movie.title} - {self.room} ({self.start_time.strftime('%d/%m %H:%M')})"