from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)  # Ruta donde se almacenarán las imágenes de perfil

    def __str__(self):
        return f"{self.user.username} Profile"
    
class ConfiguracionEscolar(models.Model):

    distrito = models.CharField(max_length=100, verbose_name="Distrito")
    nombre_escuela = models.CharField(max_length=100, verbose_name="Nombre de la escuela")
    numero = models.CharField(max_length=20, verbose_name="Número")

    sector_gestion = models.CharField(
        max_length=20,
        choices=[('Estatal', 'Estatal'), ('Privado', 'Privado')],
        default='statal',
        verbose_name="Sector de gestión"
    )
    
    clave_provincial = models.CharField(max_length=50, verbose_name="Clave provincial")
    cue = models.CharField(max_length=50, verbose_name="CUE")

    class Meta:
        verbose_name = "Configuración Escolar"
        verbose_name_plural = "Configuración Escolar"  # Para que no muestre "Configuracion Escolars" en el admin

    def save(self, *args, **kwargs):
        # Fuerza que solo exista un registro
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        # Carga o crea la única instancia
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    def __str__(self):
        return f"Configuración de {self.nombre_escuela}"