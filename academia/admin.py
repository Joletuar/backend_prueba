from django.contrib import admin
from .models import Aula, Profesor, Materia


@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ("fecha", "hora", "tema", "profesor", "materia")
    search_fields = ("fecha", "hora", "tema", "profesor", "materia")
    list_filter = ("fecha", "hora", "tema", "profesor", "materia")
    ordering = ("fecha", "hora", "tema", "profesor", "materia")


@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    search_fields = ("nombre", "descripcion")
    list_filter = ("nombre", "descripcion")
    ordering = ("nombre", "descripcion")


@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "correo")
    search_fields = ("nombre", "correo")
    list_filter = ("nombre", "correo")
    ordering = ("nombre", "correo")
