# Generated by Django 2.0 on 2018-07-24 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barberos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuenta',
            name='tipo',
            field=models.CharField(blank=True, choices=[('A', 'Ahorro'), ('C', 'Corriente')], max_length=1),
        ),
    ]