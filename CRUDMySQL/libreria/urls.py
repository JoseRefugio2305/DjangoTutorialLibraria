from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns=[
    path('', views.index,name='Index'),
    path('libros', views.libros,name='Libros'),
    path('libros/Add_Book_Form', views.Add_Book_Form,name='Add_Book_Form'),
    path('libros/Edit_Book_Form', views.Edit_Book_Form,name='Edit_Book_Form'),
    path('libros/Edit_Book_Form/<int:id>', views.Edit_Book_Form,name='Edit_Book_Form'),
    path('libros/Delete_Book/<int:id>', views.eliminar,name='EliminarLibro'),
    path('AboutUs/', views.AboutUs,name='AboutUs')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)#Configuyraciones para rutas de visualizacion de imagenes