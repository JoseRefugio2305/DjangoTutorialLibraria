# Tutorial usado

[Sitio web con python | CRUD django mysql](https://youtu.be/ezIj71CX944)

# Iniciando Proyecto

Para iniciar un nuevo proyecto se ejecuta el comando
~~~
django-admin startproject nombre_proyecto
~~~

# Creando aplicacion dentro del proyecto

~~~
python manage.py startapp nombre_app
~~~

# Inciando Servidor

~~~
python manage.py runserver
~~~

# Migraciones
Una vez se crean los modelos y se hace la conexion a la base de datos, se llevan a cabo las migraciones con el comando:

~~~
python manage.py makemigrations NombreApp
python manage.py migrate NombreApp
~~~

En la ruta de la aplicacion principal. Esto hace que en base de datos se creen las tablas que corresponden a los modelos.

El primer comando prepara las migraciones y el segundo las lleva a cabo y las refleja en base de datos tambien.

Esto ademas crea demas tablas que son necesarias para el apartadode administrador que ofrece django.

Cada vez que se haga un cambio al modelo, se debe de llevar a cabo de nuevo la migracion. Esto hara que el cambio tambien se refleje en base de datos.

# Preparacion de usuario administrador
Para crear el usuario se ejecuta el siguiente comando:

~~~
python manage.py createsuperuser
~~~

Este comando al ser ejecutado pide la informacion necesaria para crear el usuario.

# Conexion a Base de Datos MySQL

Dentro del archivo settings.py de la aplicacion principal, se debe de agregar los datos de la conexion.
~~~python 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'libreria',
        'USER':'root',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT':'3306'
    }
}
~~~

En el archivo __init__.py de la misma aplicacion principal, se debe agregar lo siguiente para inicializar el cliente de la conexion PyMySQL

~~~python
import pymysql

pymysql.install_as_MySQLdb()#Esto es para poder interactuar con la base de datos, sin esta instalacion da error
~~~