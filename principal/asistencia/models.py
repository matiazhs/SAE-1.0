from django.db import models # type: ignore
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator # type: ignore
from django.core.exceptions import ValidationError # type: ignore
from alumnos.models import Alumno, Turno


class TipoAsistencia(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Asistencia(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    fecha = models.DateField()
    #turno = models.ForeignKey(Turno, on_delete=models.PROTECT)
    tipo = models.ForeignKey(TipoAsistencia, on_delete=models.PROTECT)
    
    TIPO_ASISTENCIA_CHOICES = [
        ("P", "Presente"),
        ("A", "Ausente"),
        ("T", "Tarde"),
        ("AP", "Ausente con presencia"),
    ]

    estado = models.CharField(
        max_length=2,
        choices=TIPO_ASISTENCIA_CHOICES,
        default="P"
    )

    class Meta:
        unique_together = ("alumno", "fecha", "tipo")

    def __str__(self):
        return f"{self.alumno} - {self.fecha} - {self.tipo}: {self.get_estado_display()}"
