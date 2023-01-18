# Generated by Django 4.1.5 on 2023-01-17 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=150, verbose_name='Título')),
                ('descripcion', models.TextField(null=True, verbose_name='Descripción ')),
                ('imagen', models.ImageField(null=True, upload_to='../static/libros/', verbose_name='Imagen')),
                ('added_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
