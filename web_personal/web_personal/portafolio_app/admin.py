from django.contrib import admin
# importar modelo de la aplicacion
from .models import proyecto

class Proyecto_admin(admin.ModelAdmin):
    read_only_fields = ("fecha_creacion", "fecha_modificacion")

# Register your models here.
admin.site.register(proyecto, Proyecto_admin)


