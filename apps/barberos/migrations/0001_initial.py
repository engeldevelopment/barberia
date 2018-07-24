# Generated by Django 2.0 on 2018-07-24 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Barbero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('apodo', models.CharField(max_length=30)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=15)),
                ('barbero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barberos.Barbero')),
            ],
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=22, unique=True)),
                ('banco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barberos.Banco')),
                ('barbero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barberos.Barbero')),
            ],
        ),
    ]
