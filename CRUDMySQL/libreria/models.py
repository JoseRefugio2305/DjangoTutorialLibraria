from django.db import models

# Create your models here.
class Libro (models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=150, verbose_name='Título')#verbose_name es para indicar el nombre del campo al usuario mostrandoselo
    descripcion=models.TextField(null=True,verbose_name='Descripción ')
    imagen=models.ImageField(upload_to='static/img/',verbose_name='Imagen', null=True)
    added_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        fila='Título: '+self.titulo +' - Descripoción: '+self.descripcion[:16]+'...'
        return fila
    #Lo siguiente es para que cuando se borre un registro tambien se borre de la aplicacion la imagen que correspondia a el
    def delete(self,using=None,keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()