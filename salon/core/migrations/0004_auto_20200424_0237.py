# Generated by Django 3.0.5 on 2020-04-24 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200424_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='servi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Servicio'),
        ),
    ]
