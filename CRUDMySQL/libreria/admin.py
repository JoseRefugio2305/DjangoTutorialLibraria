from django.contrib import admin
from .models import Libro

# Register your models here.
admin.site.register(Libro)#Aqui agregamos el modelo para que el administrador pueda verlo en su vista del sistema y pueda agregar o modificar informacion de los libros