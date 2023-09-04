from django.db import models


class Profesor(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    correo = models.EmailField(blank=False, null=False)

    def __str__(self):
        return self.nombre


class Materia(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.nombre


class Aula(models.Model):
    fecha = models.DateField(blank=False, null=False)
    hora = models.TimeField(blank=False, null=False)
    tema = models.CharField(max_length=200, blank=False, null=False)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

    def __str__(self):
        return f"Aula {self.fecha} - {self.hora}: {self.tema}"
