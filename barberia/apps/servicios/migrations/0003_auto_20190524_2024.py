# Generated by Django 2.1.4 on 2019-05-24 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0002_servicio_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='foto',
            field=models.ImageField(blank=True, default='web/img/2.jpeg', null=True, upload_to='servicios'),
        ),
    ]
