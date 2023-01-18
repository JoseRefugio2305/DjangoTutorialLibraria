from django import forms
from .models import Libro


class LibroForm(forms.ModelForm):
    class Meta:
        model=Libro
        fields='__all__'#Aqui especificamos que use todos los campos, en caso de que solo se quiere usar algunos de ellos, se deben especificar en un arreglo

