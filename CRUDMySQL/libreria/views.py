from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm
# Create your views here.

def index(request):
    return render(request, 'index.html',{'title':'Bienvenido A La Librería'})

def libros(request):
    libros=Libro.objects.all()
    return render(request, 'libros.html',{
        'libros':libros,
        'title':'Listado de Libros'
        })

def AboutUs(request):
    return render(request, 'aboutus.html',{'title':'Acerca de Nosotros'})

def Add_Book_Form(request):
    formulario=LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('Libros')#En el redirect va el nombre que se le dio a la ruta en urls.py en name=''
    return render(request, 'create.html',{'formulario':formulario,'title':'Agregar Libro'})

def Edit_Book_Form(request,id):
    libro=Libro.objects.get(id=id)
    formulario=LibroForm(request.POST or None, request.FILES or None, instance=libro)#Le decimos que llene los cmapos con la informacion dle obtejo libro a editar
    if formulario.is_valid() and request.method=='POST':
        formulario.save()
        return redirect('Libros')
    return render(request, 'editar.html',{'formulario':formulario,'title':'Editar Libro'})

def eliminar(request, id):
    libro=Libro.objects.get(id=id)
    libro.delete()
    return redirect('Libros')