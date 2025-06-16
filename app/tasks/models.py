from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Tarea(models.Model):
    ESTADOS = [
        ('P', 'Pendiente'),
        ('EP', 'En Progreso'),
        ('C', 'Completado'),
    ]

    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    estado = models.CharField(max_length=2, choices=ESTADOS, default='P')
    fecha_vencimiento = models.DateField()
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='tareas')
    responsable = models.CharField(max_length=100)

    def clean(self):
        if self.fecha_vencimiento and self.fecha_vencimiento < timezone.now().date():
            raise ValidationError("La fecha no puede ser en el pasado")

    def __str__(self):
        return f"{self.nombre} ({self.get_estado_display()})"

    class Meta:
        ordering = ['fecha_vencimiento']

