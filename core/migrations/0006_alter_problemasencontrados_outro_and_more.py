# Generated by Django 4.2.6 on 2023-12-01 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_ocorrenciatipo_queda_altura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemasencontrados',
            name='outro',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='problemasencontrados',
            name='respiratorio',
            field=models.BooleanField(default=False),
        ),
    ]
