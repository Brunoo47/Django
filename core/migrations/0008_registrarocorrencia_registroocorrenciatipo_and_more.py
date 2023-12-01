# Generated by Django 4.2.6 on 2023-12-01 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_problemasencontrados_registroid'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrarocorrencia',
            name='registroOcorrenciaTipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.ocorrenciatipo'),
        ),
        migrations.AddField(
            model_name='registrarocorrencia',
            name='registroProblemasEncontrados',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.problemasencontrados'),
        ),
    ]