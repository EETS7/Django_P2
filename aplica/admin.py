from django.contrib import admin
from aplica.models import uno
class UsuarioAdmin(admin.ModelAdmin):
    list_display=("Nombre","Numero","Intentos")
    search_fields=("Nombre","Numero","Intentos")

admin.site.register(uno,UsuarioAdmin)
# Register your models here.
