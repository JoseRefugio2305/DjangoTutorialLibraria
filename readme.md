# Migraciones
Una vez se crean los modelos y se hace la conexion a la base de datos, se llevan a cabo las migraciones con el comando:

python manage.py makemigrations

python manage.py migrate

En la ruta de la aplicacion principal. Esto hace que en base de datos se creen las tablas que corresponden a los modelos.

El primer comando prepara las migraciones y el segundo las lleva a cabo y las refleja en base de datos tambien.

Esto ademas crea demas tablas que son necesarias para el apartadode administrador que ofrece django.

Cada vez que se haga un cambio al modelo, se debe de llevar a cabo de nuevo la migracion. Esto hara que el cambio tambien se refleje en base de datos.

# Preparacion de usuario administrador
Para crear el usuario se ejecuta el siguiente comando:

python manage.py createsuperuser

Este comando al ser ejecutado pide la informacion necesaria para crear el usuario.


