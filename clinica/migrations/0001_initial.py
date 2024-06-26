# Generated by Django 5.0.4 on 2024-04-11 14:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id_especialidade', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=256)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id_medico', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=256)),
                ('endereco', models.TextField()),
                ('telefone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('data_nascimento', models.DateField()),
                ('crm', models.CharField(max_length=12)),
                ('especialidade_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='clinica.especialidade')),
            ],
        ),
    ]
